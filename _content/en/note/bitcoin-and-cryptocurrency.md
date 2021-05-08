---
categories: [Programming]
date: 2021-04-19
keywords: [blockchain, transaction, bitcoin, transactions, decentralized, consensus,
  nodes, block, network, hash]
lang: en
recommendations: [/note/coursera-blockchain-specialization/, /note/iotswc-2019/, /note/becoming-a-product-manager/]
title: Learning Cryptocurrency with Code
---

In "**[What Blockchain Brings to Real-World Applications](/note/coursera-blockchain-specialization/)**", I learned blockchain basics ranging from cryptography and hashing to smart contracts and decentralized applications using the Solidity programming language. For me, one of the most important findings was the diversity of blockchain applications; cryptocurrency like Bitcoin is not the only application blockchain makes possible, and the technology resolves a wide variety of real-life problems in a decentralized manner as long as:

1. trust among unknown peers in a network matters;
2. the situation requires validation, verification, recording of time-stamped immutable conditions.

On the other hand, there is another online course "[Bitcoin and Cryptocurrency Technologies](https://www.coursera.org/learn/cryptocurrency)" offered by Princeton University, which focuses purely on blockchain technologies for money transactions. The content is fully based on their [textbook](https://bitcoinbook.cs.princeton.edu/), and the course gives us highly detailed (mostly theoretical) explanations of how & why Bitcoin works.

The advanced course has covered a couple of notable topics as follows, and the coding exercises helped me to have a clear picture of how (1) transaction is verified, (2) consensus is made, and (3) block (i.e., set of transactions) is created & added to a chain.

### Why Bitcoin works

Bitcoin's security relies on the difficulty of resolving the hash puzzle, and the difficulty even changes dynamically as nodes in the network automatically re-calculates their targets about every two weeks; finding a hash below a given target within the period is probabilistically impossible. 

Moreover, the use of Bitcoin is all about "keys". Since there is no intermediary in the Bitcoin network, how individual nodes store/use their coins is tied to how their private key and user's addresses (public keys) are retained/accessed. Such consideration leads to a concept of hot and cold wallet storage, and it enables Bitcoin users to store their BTC in online wallets and exchange them with others.

To be more precise, the following code snippets provided in the course illustrate how blockchain works with hashes and keys. 

First, a single block consists of multiple transactions, and the block memorizes a "hash" of its previous block and "address" a coinbase transaction goes so that the blocks properly form *a chain*:

```java
public class Block {
    public static final double COINBASE = 25;

    private byte[] hash;
    private byte[] prevBlockHash;
    private Transaction coinbase;
    private ArrayList<Transaction> txs;

    public Block(byte[] prevHash, PublicKey address) {
        prevBlockHash = prevHash;
        coinbase = new Transaction(COINBASE, address);
        txs = new ArrayList<Transaction>();
    }

    // ...
}
```

Note that a coinbase transaction is the first transaction in a block created by a miner, and the amount (e.g., `25` in this example) is determined by a blockchain. 

Additionally, individual transactions are made of input and output transactions, and each of them is associated with "hashes" and "public key" of its origin and recipient:


```java
public class Transaction {

    public class Input {
        /** hash of the Transaction whose output is being used */
        public byte[] prevTxHash;
        /** used output's index in the previous transaction */
        public int outputIndex;
        /** the signature produced to check validity */
        public byte[] signature;
    
        // ...
    }

    public class Output {
        /** value in bitcoins of the output */
        public double value;
        /** the address or public key of the recipient */
        public PublicKey address;
    
        // ...
    }

    private byte[] hash;
    private ArrayList<Input> inputs;
    private ArrayList<Output> outputs;
    private boolean coinbase;

    // ...
}
```

### It's a currency

Bitcoin itself doesn't explicitly solve a distributed consensus problem, but it rather introduces a concept of "financial incentive" that motivates miners to (1) validate transactions, (2) store and broadcast blockchain, and (3) vote on consensus. Eventually, a consensus has to be reached over a long time scale by propagating miners' work. Bitcoin does have a financial meaning as a currency&mdash;That's why the incentive lets miners help to make consensus in a decentralized fashion.

It should be noticed that the connections among nodes in the blockchain network can be modeled as a random directed graph. That is, at the broadcasting phase, the nodes make a consensus by repeatedly sending (receiving) transactions to followers (from followees) until their observations converge. 

To verify a transaction, assume `UTXO` and `UTXOPool utxoPool` are respectively the representation of a single Unspent Transaction Output (UTXO) and a valid set of UTXOs from the previous block. Here, given the `Transaction` class above, the course has defined that a single transaction `Transaction tx` is valid **only if** all of the following conditions are true:

1. all outputs claimed by `tx` are in the current `utxoPool`;
  - For each `Transaction.Input in`, make sure `UTXO ut = new UTXO(in.prevTxHash, in.outputIndex)` is in `utxoPool`.
2. the signatures on each input of `tx` are valid;
  - For `Transaction.Ouput out` retrieved from `utxoPool` by `ut`, make sure a signature derived by `out.address` equals to `in.signature`.
3. no UTXO is claimed multiple times by `tx` (i.e., double-spending is not allowed);
  - Every input `in` is unique in the transaction `tx`.
4. all of `tx`'s output values are non-negative;
5. the sum of `tx`'s input values is greater than or equal to the sum of its output values.

_\* See **[gist](https://gist.github.com/takuti/50ef664cf49fc0a0c32bcca095b15062)** for full implementation of transaction handler._

### Scalability matters

Speaking of limitations, miner's work is computationally expensive. To give an example, the Bitcoin blockchain network can process about 7 transactions/sec (as of the course is created), whereas the global transaction system of Visa credit cards shows a much higher throughput of 2k-10k transactions/sec[^1]. As we see many "hash", "signature", and "address" related operations in the code snippets above, the operations are repeatedly executed for every single transaction in the network.

The fact naturally accelerates the development of mining hardware (e.g., GPU, FPGA, ASIC), which enables miners to more efficiently calculate hashes and have a better chance of receiving large incentives. Meanwhile, the dynamics force the blockchain to adjust the design by forking because the current assumption about the difficulty of calculating hashes and signatures won't work when we encounter excessive computing power. Ultimately, the rise of quantum computing certainly threatens the whole system.

Note that the discussion poses a new challenge about its energy consumption as [Bill Gates has recently warned](https://www.technologyelevation.com/2021/03/bill-gates-says-that-bitcoin-is-bad-for.html). I personally feel mining blockchain efficiently in terms of energy use is one of the biggest topics the community must tackle, as blockchain and cryptocurrency are widely democratized these days.

### Beyond cryptocurrencies

Last but not least, the course does mention about the blockchain applications beyond cryptocurrencies, such as decentralized property ownership (a.k.a. smart property). In particular, a framework blockchain application developers can follow seems to be useful:

> ***Decentralizes*** *(what)* ***in the sense of*** *(level of decentralization)* ***using*** *(coin type)* ***via*** *(security property)*

- ***Decentralizes*** *(what)*
  - Purely digital things where blockchain can be used as a state in the digital world (e.g., storage, pay for proof, random number generator, lotteries)
  - Things that can be represented digitally (e.g., real-world currencies, stocks)
  - Property ownership and trade
  - Complex contracts (e.g., crowd funding, financial derivatives)
  - Markets and auctions (i.e., matching system)
  - Data feeds, a system that works as a trustable data source
  - Autonomous agents (e.g., for contracts and voting)
  - Exchanges (e.g., currency exchange with strangers)
- ***in the sense of*** *(level of decentralization)*
  1. Single mandatory intermediary
  2. Multiple competing intermediaries
  3. "Threshold" of intermediaries
  4. No intermediary 
- ***using*** *(coin type)*
  - Directly on Bitcoin (limited representation)
  - Embedding; colored coin (limited scripting)
  - Side chained coin
  - AltCoins like Ethereum
- ***via*** *(security property)*
  - Atomicity exchange
  - Reputation
  - Escrow for dispute handling & mediation

If a problem enables us to intuitively fill the sentence, there is a chance of innovation.

Although understanding blockchain technologies is not straightforward, the combination of high-level introduction "[Blockchain Specialization](https://www.coursera.org/specializations/blockchain)" and advanced hands-on experience "[Bitcoin and Cryptocurrency Technologies](https://www.coursera.org/learn/cryptocurrency)" helped me to get a better sense of the complex topic a lot. In addition to the possibility of cryptocurrencies many people can easily think of, I strongly believe the field unlocks numerous opportunities that a decentralized system can change.

[^1]: Of course, the credit card system works in a centralized manner, and comparing the Blockchain decentralized network with Visa is a bit unfair.
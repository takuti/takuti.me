---
categories: [Programming]
date: 2021-04-11
images: [/images/coursera-blockchain-specialization/blockchain-overview.png]
lang: en
title: What Blockchain Brings to Real-World Applications
keywords: [blockchain, decentralized, smart, transactions, specialization, contract,
  application, validation, transaction, solidity]
recommendations: [/note/bitcoin-and-cryptocurrency/, /note/iotswc-2019/, /note/web3/]
---

I have [completed **Blockchain Specialization**](http://coursera.org/verify/specialization/ZN492RNBJQAM) offered by University at Buffalo on Coursera. 

So, what is blockchain?

It's a set of techniques that makes secure P2P transactions possible among distributed nodes in a decentralized system. By leveraging the methods for validation, verification, consensus, and immutable recording, blockchain allows us to establish trust with unknown peers.

That is, if trust among unknown peers in a network matters and the situation requires validation, verification, recording of time-stamped immutable conditions, blockchain can be a deeply satisfying way to build an appropriate solution to the problem.

### Motivation

This specialization became my first hands-on blockchain experience, and I was particularly curious about how the concept is applied to real-world problems.

To give an example, [Supply Chain Management Specialization](/note/coursera-supply-chain-management/) told me that a core of real-world supply chain is all about a holistic optimization process from sourcing and planning to operations and logistics. It means that establishing trustable, efficient mutual relationships among individual roles (e.g., procurement department, supplier, truck driver) is a fundamental requirement for the whole system. Here, connecting people and relaying assets can respectively be considered as nodes and transactions in the blockchain world, and blockchain techniques help to make the process more transparent and reliable for everyone ranging from a raw material supplier to a consumer.

Meanwhile, when I attended [IoT Solutions World Congress 2019](/note/iotswc-2019/), I realized blockchain is becoming an important concept to ensure transparency and reliability of massively deployed complex IoT systems. It is obvious that an IoT system installs many tiny devices in a geographically distributed manner, and strangers randomly interact with them. Eventually, the system generates a large volume of data associated with human behaviors, but how can we trust the insights and overcome the privacy concerns?

Blockchain Specialization helped me to go one level deeper in these considerations and imagine how to apply the techniques to realistic problems.

### Overview

The specialization is structured as follows:

1. Blockchain Basics
2. Smart Contracts
3. Decentralized Application
4. Blockchain Platforms

After reviewing a few important concepts as follows, the courses particularly focused on implementing smart contracts for [Ethereum](https://ethereum.org/en/) blockchain using [Solidity](https://docs.soliditylang.org/en/latest/) programming language. 

- Representation of transactions in a blockchain, consisting of more than one input and output Unspent Transaction Outputs (UTXOs)
- Validity of transactions (e.g., avoid double-spending) 
- Purpose of mining blockchain: Validating computations, collecting them to form a block, verifying them, and broadcasting them.
- Roles of minors: Computers that execute operations defined by the blockchain protocol are the minors.
- Proof of Work (PoW): Certain fees are defined for mining operations, and the operations conducted by winning minors are incentivized.
- Standard process of creating a block in a blockchain:
  1. Initiate a transaction
  2. Validate the transaction
  3. Bundle and broadcast the transaction
  4. Solve PoW consensus
  5. Add a block to the local chain and propagate it to the network
- Basics of: 
  - P2P decentralized system and broadcasting 
  - Cryptography (e.g., RSA and ECC)
  - Digital signature
  - Hashing by Merkle tree
  - Distributed hash table
- Soft and hard fork of a blockchain

Sounds like fun, doesn't it? Blockchain is a frontier that combines many different techniques in the field of computer science.

### Smart contract expands the possibility of blockchain

A smart contract is an immutable, trusted, validated piece of code written in a high-level programming language, and the code can be executed by any nodes in a blockchain via its virtual machines. It is important to note that all transactions following the contracts are radically transparent and readily accessible in the blockchain.

Unlike [Bitcoin](https://bitcoin.org/), one of the most popular blockchains that can be used only for money transactions, smart contracts enable a blockchain to define complex application-specific validation logic. Ethereum, for example, can be applied not only for sending money but also for business applications like supply chains thanks to Solidity's high expressiveness. 

In the specialization, we exercised Solidity in [Remix IDE](http://remix.ethereum.org/). For me, one of the most unique capabilities Solidity offers is "modifier" (i.e., pre-defined validation logic that can revert unacceptable transactions). The capability emphasizes a fact that blockchain needs to run autonomously once it's deployed; the embedded validation logic allows the code to automatically and efficiently check if a transaction is accepted or not based on the rules, policies, and regulations defined from the beginning.

In other words, a smart contract is like a hardware chip rather than modern software; once it's deployed, updates happen infrequently, and hence we need to ensure that the code runs for a long time without modifying.

### Blockchain is just a tool

What I like about the course is that they emphasized how focusing on a problem is important for us to apply blockchain techniques. Here is a suggested process of building a blockchain application using smart contracts:

1. Start from a problem statement
2. Analyze the problem
3. Design class(es) in smart contract
4. Define visibility of variables and functions
5. Define access modifiers for the functions
6. Define validations for input variables of individual functions
7. Define conditions that must hold true

Just like the other advanced techniques (e.g., machine learning), blockchain is not a silver bullet that can resolve arbitrary problems. We must first understand that the blockchain applications are particularly suitable for:

- decentralized problems;
- P2P transactions;
- going beyond boundaries of trust among unknown peers;
- a situation that requires validation, verification, recording of time-stamped immutable network conditions.

Once we decided to use blockchain to tackle a problem, we could refer to a list of best practices/tips the specialization told us:

- Keep smart contract code simple and auditable (e.g., by using modifiers)
- Retain only the necessary data
- Use appropriate data types
- Use `int` type for most arithmetic needs
- Functions can have many modifiers
- Use events for notification
- Use secure hashing such as `keccak256` and `sha256`
- Minimize a state that contains a hash and its footprint
  - Mining fee is determined by the number of variables and functions, and hence inefficient implementation leads to unnecessary mining costs.
  - In Solidity, a scope `memory` is for any transient data, whereas `storage` is only for something that needs to persist.
- Consciously manage lifetime and ownership of smart contact (e.g, by delete, kill, transfer operations)

### Decentralized application: Frontend receives events emitted by smart contract

A smart contract can emit an event, and a client application so-called "decentralized application" listens & reacts against these events. How to implement the frontend decentralized application is one of the most interesting areas of blockchain technologies. 

To explorer the possibility of decentralized application, we tried [Truffle](https://www.trufflesuite.com/) and [Metamask](https://metamask.io/) in the course based on an RPC connection between blockchain server and Node.js-based web application using [`web3.js`](https://web3js.readthedocs.io/).

It's also interesting to see some standards in the decentralized applications e.g., Ethereum Improvement Proposal (EIP). For instance, ERC (Ethereum Request for Comment) 20 is defined for a fungible token that is replaceable, interchangeable value (e.g., `$1` = `$1`, `1BTC` = `1BTC`). Meanwhile, ERC 721 is defined as a non-fungible token standard that can be applied for non-trivial asset exchanges e.g., [Cryptokittes](https://www.cryptokitties.co/).

Moreover, if we leverage an interplanetary file system (IPFS; e.g., [go-ipfs](https://github.com/ipfs/go-ipfs)), we can transfer and store files in the decentralized fashion. Unlike HTTP that identifies a file location by its address, IPFS identifies the location by a hash of the content.

### Permissioned blockchain for the business use

At the end of the specialization, they introduced a concept of permissioned (consortium) blockchain; permissioned blockchain is a special type of blockchain that communicates only with permitted nodes, and it's particularly suitable for business scenes requiring private communications.

Such flexibility can be achieved by using [Hyperledger](https://www.hyperledger.org/) ([Fabric](https://www.hyperledger.org/use/fabric)), for example, and the service-oriented architecture makes the decentralized applications widely applicable in the B2B/B2C markets.

The other use case-specific decentralized platforms include:

- [Augur](https://augur.net/)
  - Prediction market platform
  - Roles in the platform: Market creator, trader, reporter
  - Incentivize participants based on unique criteria e.g., those who submitted good reports
- [Grid+](https://gridplus.io/)
  - IoT-specific platform in an energy ecosystem
  - Eliminate intermediaries in the energy market
  - Intelligently manage the electricity usage

These applications pose unique challenges for ensuring integrity and scalability, and hence there are still so many unexplored areas we can contribute.

### Bottom line

The specialization was well-structured for the following reasons.

- Videos are succinct and focusing on essential concepts we should know before working on blockchains.
- There is a good balance between quizzes and coding assignments.
- In coding exercises using Solidity language, we don't need to spend too much time on boring basic syntax stuff, and they rather nicely abstracted key concepts we must know before contributing to the blockchain communities.

As the professor depicted, blockchain is certainly one of the most exciting areas in computer science because the topic requires us to comprehensively understand and combine many different techniques ranging from security and privacy to data structures and distributed systems.

![blockchain](/images/coursera-blockchain-specialization/blockchain-overview.png)

Now, we understand what blockchain is, how it works, and how to apply blockchain to business problems. It's time to learn more about [real-world examples of decentralized applications](https://www.stateofthedapps.com/) and dig deep into the combination of blockchain and supply chain & IoT to satisfy my original curiosity. 
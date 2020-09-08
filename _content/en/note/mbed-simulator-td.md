---
categories: [Programming]
date: 2018-11-02
lang: en
recommendations: [/note/hivemall-events-2018-autumn/, /note/data-leaders-summit-europe-2019/,
  /note/umap-2019/]
title: Sending Sensor Data from Mbed Simulator to Treasure Data
---

[Arm Pelion IoT Platform](https://www.arm.com/products/iot/pelion-iot-platform) makes the Mbed ecosystem much more sophisticated and enables us to seamlessly manage IoT connectivity, device and data at a unified place:

![Pelion Overview](/images/arm/pelion-overview.jpg)

### Treasure Data: A Pelion data management service

My recent experience at [Mbed Connect USA](/note/hivemall-events-2018-autumn/) tells me how people show a strong interest in advanced big data management and analytics capability of [Treasure Data](https://www.treasuredata.com/) (TD) as a part of the Pelion family:

https://twitter.com/takuti/status/1052270115956305920

On that point, there is a [great demo](https://github.com/BlackstoneEngineering/mbed-os-example-treasuredata-rest) that shows how to send device health data from your Mbed devices to the Treasure Data platform via WiFi network:

![Mbed to TD](/images/arm/mbed-simulator-td/mbed-to-td.png)

Once data points emitted from your devices are securely stored to the platform, you will become able to gain tons of deeper insights at scale in combination with many different types of datasets (e.g., user's demographics and behavior) loaded from a variety of [data sources](https://www.treasuredata.com/integrations/).

To those who still don't have a physical Mbed device (including me!), this article introduces a handy version of the Mbed-to-TD data ingestion demo running on top of [Mbed simulator](https://github.com/janjongboom/mbed-simulator).

My demo code is available at: [takuti/**mbed-os-example-treasure-data**](https://github.com/takuti/mbed-os-example-treasure-data)

### Mbed simulator

**Mbed simulator** is a Node.js application which allows running our Mbed project written in C++ on a web browser:

![Mbed simulator](/images/arm/mbed-simulator-td/simulator.png)

[Emscripten](https://github.com/kripken/emscripten), an LLVM to JavaScript compiler, technically plays an important role in this application. See an [introductory article](https://os.mbed.com/blog/entry/introducing-mbed-simulator/) for more information.

Modifying sample C++ code in the editor view, and rebuilding and executing it on a simulated Mbed device are quite easy. Additionally, once you properly define a `simconfig.json` config file for a time of compilation, the simulator enables working with peripherals such as [LCD](https://os.mbed.com/components/128x32-LCD/) and [temperature & humidity sensor](https://os.mbed.com/components/SHT31-D/).

### Periodically posting data point to TD

Following C++ code is a basic template that periodically sends JSON-formatted data point to TD:

```cpp
#include "mbed.h"
#include "EthernetInterface.h"
#include "http_request.h"

#define URL_SIZE 200
#define BODY_SIZE 100

#define TD_SEND_INTERVAL 10

const char *td_database = "TARGET_DATABASE_NAME";
const char *td_table = "TARGET_TABLE_NAME";
const char *td_apikey = "YOUR_API_KEY";

int main(void) {
  // Connect with Ethernet
  EthernetInterface network;
  if (network.connect() != 0) {
    printf("Cannot connect to the network\n");
    return 1;
  }

  // Assemble URL: https://support.treasuredata.com/hc/en-us/articles/360000675487-Postback-API
  char url[URL_SIZE];
  sprintf(url, "http://in.treasuredata.com/postback/v3/event/%s/%s", td_database, td_table);

  char body[BODY_SIZE];

  // Get data, send to Treasure Data every TD_SEND_INTERVAL seconds
  while (1) {
    float value1 = // ...
    float value2 = // ...

    // Construct JSON string to send
    sprintf(body, "{\"column1\":%f,\"column2\":%f}", value1, value2);

    // Send data to Treasure data
    {
      HttpRequest *req = new HttpRequest(&network, HTTP_POST, url);
      req->set_header("Content-Type", "application/json");
      req->set_header("X-TD-Write-Key", td_apikey);

      HttpResponse *res = req->send(body, strlen(body));
      if (!res) {
        printf("HttpRequest failed (error code %d)\n", req->get_error());
        return 1;
      }

      delete req;
    }

    wait(TD_SEND_INTERVAL);
  }

  network.disconnect();
}
```

Similarly to the [device health demo](https://github.com/BlackstoneEngineering/mbed-os-example-treasuredata-rest), this template simply sends a HTTP POST request to TD's [postback API](https://support.treasuredata.com/hc/en-us/articles/360000675487-Postback-API) as [mbed-os-example-http](https://os.mbed.com/teams/sandbox/code/http-example/) does.

Depending on JSON-formatted content body, a wide variety of device/sensor data can be incrementally ingested to arbitrary Treasure Data account, database and table.

### Sending temperature & humidity data to TD

In order to make a demo scenario more motivating, add a dummy temperature and humidity sensor to the simulator:

![Mbed TD simulator](/images/arm/mbed-simulator-td/simulator-td.png)

`while` loop in the template will be:

```cpp
  int cnt = 1;
  while (1) {
    lcd.cls();

    float temp = sht31.readTemperature();
    float humidity = sht31.readHumidity();

    lcd.locate(2, 2);
    lcd.printf("Sent %d records to TD", cnt++);
    lcd.locate(2, 12);
    lcd.printf("Temperature: %.2f C", temp);
    lcd.locate(2, 22);
    lcd.printf("Humidity: %.2f %%", humidity);

    // Construct strings to send
    sprintf(body, "{\"temperature\":%f,\"humidity\":%f}", temp, humidity);

    // Send data to Treasure data
    {
      ...
    }

    wait(TD_SEND_INTERVAL);
  }
```

It's time to imitate the change of environmental condition by clicking the sensor component:

![Image from Gyazo](https://i.gyazo.com/59b7426607b7e995fe4d477db5c61df5.gif)

Data point is accordingly sent to your TD table every 10 seconds as LCD displays, and it's soon to be available on the data management service as:

![Records on TD](/images/arm/mbed-simulator-td/records.png)

Super simple and easy, isn't it?

Again, the full demo implementation and installation guide are available at a [GitHub repository](https://github.com/takuti/mbed-os-example-treasure-data), and you can **immediately** try this sample **on your browser**.

### What's next?

Sending sensor data to the platform is not our goal for sure; there are many possibilities we can do from here.

Importantly, Treasure Data provides [Presto](https://support.treasuredata.com/hc/en-us/articles/360001457427-Presto-Query-Engine) and [Hive](https://support.treasuredata.com/hc/en-us/articles/360001457347-Hive-Query-Language) query interface for users to easily access to their massive data at scale, as well as a bunch of [third-party data integrations](https://www.treasuredata.com/integrations/). Hence, in case of the temperature and humidity data, the platform could be used to:

- Compute average value per month, and see how local environmental condition changes over time in the monthly basis.
- Build temperature/humidity predictor by using TD's [ML capability](https://support.treasuredata.com/hc/en-us/categories/360001001934-Machine-Learning), and predict future wether condition near the sensor.
- Send an alert to people who are living within a mile radius from the sensor, when recent data points show exceptionally high/low value.

Meanwhile, in reality, we can do more at device-side such as:

- Allocating more sensors across a city, and attaching their identifier and/or geolocation to emitted data.
- Deploying pre-built ML model to the devices, and make edge-side prediction (e.g., anomaly detection) with [uTensor](https://github.com/uTensor/uTensor).

In any scenarios, I personally believe that integration between Treasure Data and Mbed OS would become one of the most important and exciting challenges for all Mbed developers in near future.
const https = require("https");
const fs = require("fs");

const options = {
  hostname: "cn.bing.com",
  port: 443,
  path: "/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=zh-CN",
  method: "GET",
};

const req = https.request(options, (bing_res) => {
  let bing_body = [],
    bing_data = {};
  bing_res.on("data", (chunk) => {
    bing_body.push(chunk);
  });
  bing_res.on("end", () => {
    bing_body = Buffer.concat(bing_body);
    bing_data = JSON.parse(bing_body.toString());
    let img_array = bing_data.images;
    let img_url = [];
    img_array.forEach((img) => {
      img_url.push({
        url: img.url,
        copyright: img.copyright,
        copyrightLink: img.copyrightlink,
      });
    });
    var jsonpStr = "getBingImages(" + JSON.stringify(img_url) + ")";
    fs.writeFile("./assets/json/images.json", jsonpStr, (err) => {
      if (err) {
        throw err;
      }
      console.log("JSON data is saved: " + jsonpStr);
    });
  });
});

req.on("error", (error) => {
  console.error(error);
});

req.end();

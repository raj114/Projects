import { Component, OnInit } from '@angular/core';
import { BarcodeScannerOptions, BarcodeScanner } from '@ionic-native/barcode-scanner/ngx';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-office',
  templateUrl: './office.page.html',
  styleUrls: ['./office.page.scss'],
})
export class OfficePage implements OnInit{
encodeData:any;
scannedData: {};
uname:any;
barcodeScannerOptions: BarcodeScannerOptions;

constructor( private barcodeScanner: BarcodeScanner,private http: HttpClient) {
  
  //Options
  this.barcodeScannerOptions = {
    showTorchButton: true,
    showFlipCameraButton: true
  };
}
getdata(){
  let a=window.location.href;
  console.log(a);
  this.uname=a.split('/');
}
scanCode() {
  this.barcodeScanner.scan().then(barcodeData => {
    alert('Barcode data ' + JSON.stringify(barcodeData));
    this.scannedData = barcodeData;
  }).catch(err => {
    console.log('Error', err);
  });
  var myobj = {
    "encoded_text":this.scannedData,
    "user_position":this.uname[3]

  }
  console.log("post call attempt", myobj)
  this.http.post('http://35.200.130.18:8000/scandata/', 
  myobj, 
  {
    headers: { 'Content-Type': 'application/json' }
  })
  .subscribe(data => {
    console.log("response",data);
  })
}



encodedText() {
  this.barcodeScanner.encode(this.barcodeScanner.Encode.TEXT_TYPE, this.encodeData).then((encodedData) => {
    console.log(encodedData);
    this.encodeData = encodedData;
  }, (err) => {
    console.log("Error occured : " + err);
  });
  console.log(this.encodeData);
  var myobj = {
    "user_name":this.uname[4],
    "encoded_text":this.encodeData

  }
  console.log("post call attempt", myobj)
  this.http.post('http://35.200.130.18:8000/encodedata/', 
  myobj, 
  {
    headers: { 'Content-Type': 'application/json' }
  })
  .subscribe(data => {
    console.log("response",data);
  })
}


ngOnInit() {
  this.getdata();
  
}
}
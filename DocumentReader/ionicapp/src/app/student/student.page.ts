import { Component, OnInit } from '@angular/core';
import { BarcodeScanner, BarcodeScannerOptions } from '@ionic-native/barcode-scanner/ngx';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-student',
  templateUrl: './student.page.html',
  styleUrls: ['./student.page.scss'],
})
export class StudentPage implements OnInit {

  encodeData:any;
  uname:any;
  barcodeScannerOptions: BarcodeScannerOptions;
  output : any;
  
  constructor( private barcodeScanner: BarcodeScanner,private http: HttpClient) {
    
    //Options
    this.barcodeScannerOptions = {
      showTorchButton: true,
      showFlipCameraButton: true
    };
    
  }

  getdata(){
    let a=window.location.href;
    this.uname=a.split('/')
    
  }

  checkstatus(){
    this.uname = this.uname[4]
    this.http.post('http://35.200.130.18:8000/studentauth/',{'user_name':this.uname},{
    }).subscribe(data => {
      this.output = data;
    })

    console.log(this.output)
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


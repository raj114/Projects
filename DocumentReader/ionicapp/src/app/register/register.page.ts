import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiServicesService } from '../api-services.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage implements OnInit {
  username:string;
  password:string;
  mob_no:string;
  position:string;
  name:string;

  constructor(private router: Router,private api:ApiServicesService, private http: HttpClient) { }
  register(){
    var myobj = {
      "name":this.name,
      "user_name":this.username,
      "user_password":this.password,
      "user_mobilenumber":this.mob_no,
      "user_position":this.position,

    }
    // this.api.userdata(myobj).subscribe(res=>{console.log("Succses")},(err) => {
    //   console.log("Error occured : " + err);
    // });
console.log("post call attempt", myobj)
    this.http.post('http://35.200.130.18:8000/registerdata/', 
    myobj, 
    {
      headers: { 'Content-Type': 'application/json' }
    })
    .subscribe(data => {
      console.log("response",data);
    })
    location.reload();
    // console.log(this.username);
    // console.log(this.mob_no);
    // console.log(this.password);
    // console.log(this.position);
    // console.log(this.name);
    
  }
  back(){
    this.router.navigate(['/home']);
  }

  ngOnInit() {
  }

}

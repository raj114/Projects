import { Component } from '@angular/core';
import { RegisterPage } from '../register/register.page';
import { Router } from '@angular/router';
import {ApiServicesService} from '../api-services.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  username:string;
  password: string;
  position:string;
  
  constructor (private router: Router,public api : ApiServicesService,private http: HttpClient){

  }
  login(){
    if(this.username.length==0 || this.password.length==0 || this.position.length==0 ){
      alert("plz fill all details");
    }
    console.log(this.position);
    this.http.get('http://35.200.130.18:8000/userdata/'+this.username+'/'+this.password+'/',
    {
      headers: { 'Content-Type': 'application/json' }
    })
    .subscribe(data => {
      //console.log(data[0]["user_position"])
      if(data){

        this.router.navigate(["/"+data[0]["user_position"],data[0]["user_name"]])
        
      }
      else{
        alert("Invalid Login");
      }


     
    })
    
   
  }

  goregister(){
    this.router.navigate(['/Register'])
  }
}

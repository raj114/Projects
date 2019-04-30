import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiServicesService {
  baseUrl = '';

  constructor(public http: HttpClient) {}

  userdata(data):Observable<any>{
     return this.http.post(this.baseUrl,data)

  }

  genaratedcode(data):Observable<any>{
    return this.http.post(this.baseUrl,data)

 }
 
  statuscheck(data):Observable<any>{
  return this.http.post(this.baseUrl,data)

}
    }
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpEvent, HttpErrorResponse, HttpEventType } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { environment } from '../../environments/environment'
@Injectable({
  providedIn: 'root'
})
export class UploadService {


  private httpOptions: any;
  constructor(private httpClient: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({ 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' })
    };
  }


  public upload(formData: any) {
    return this.httpClient.post<any>(`${environment.SERVER_URL}/csv_uploader`, formData, {
      reportProgress: true,
      observe: 'events'
    });
  }
}
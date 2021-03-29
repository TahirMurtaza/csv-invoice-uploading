import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Invoice } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ReportService {
  private httpOptions: any;
  private handleError:any
  constructor(private http: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };
  }
  get(): Observable<Invoice[]> {
    return this.http.get<Invoice[]>(`${environment.SERVER_URL}/getinvoices`)
  }
}

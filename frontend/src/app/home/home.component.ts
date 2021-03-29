import { Component, OnInit, ViewChild, ElementRef  } from '@angular/core';
import { HttpEventType, HttpErrorResponse, HttpEvent } from '@angular/common/http';
import { of } from 'rxjs';  
import { catchError, map } from 'rxjs/operators';  
import {MatSnackBar} from '@angular/material/snack-bar';
import { UploadService } from  '../Services/upload.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})



export class HomeComponent implements OnInit {
  @ViewChild("fileUpload", {static: false}) fileUpload!:ElementRef;
  
  constructor(private uploadService: UploadService,private _snackBar:MatSnackBar){}
  output= "";
  message = "";
  ngOnInit(): void {
  }
  uploadFile(file:any) {  
    const formData = new FormData();
    console.log(file)  
    formData.append('file', file);  
     
    this.uploadService.upload(formData).subscribe((event: HttpEvent<any>) => {
      switch (event.type) {
        case HttpEventType.Sent:
          console.log('Request has been made!');
          break;
        case HttpEventType.ResponseHeader:
          console.log('Response header has been received!');
          break;
        case HttpEventType.UploadProgress:
          console.log('Uploaded!');
          console.log(event)
          break;
        case HttpEventType.Response:
          console.log('File Uploaded Successfully!', event.body);
          this.output = event.body.output;
          this.message = event.body.message;
          this.openSnackBar(this.message,"Message");
      }
    }) 
  }

  onClick() {  
    const fileUpload = this.fileUpload.nativeElement;fileUpload.onchange = () => {  
      console.log(fileUpload.files[0])
      this.uploadFile(fileUpload.files[0]);  
    };  
    fileUpload.click();  
}
openSnackBar(message: string, action: string) {
  this._snackBar.open(message, action, {
    duration: 2000,
  });
}

}

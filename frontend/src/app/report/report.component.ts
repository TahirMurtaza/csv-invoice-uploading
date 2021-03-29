import { AfterViewInit, Component, ViewChild,OnInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Invoice } from '../models/models';
import { ReportService } from '../Services/report.service';



@Component({
  selector: 'app-report',
  templateUrl: './report.component.html',
  styleUrls: ['./report.component.scss']
})

export class ReportComponent implements AfterViewInit  {
  displayedColumns: string[] = ['id', 'amount', 'due_on', 'sell_price'];
  invoices!: Invoice[];
  dataSource: MatTableDataSource<Invoice>;

  //dataSource = new MatTableDataSource<Invoice>(this.invoices);
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  
  constructor(private reportService: ReportService) {
    this.getInvoices()
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource(this.invoices);
  }
  

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
    
  }

  getInvoices() {
    this.reportService.get().subscribe(data => {
      this.invoices = data;
      this.dataSource.data = this.invoices;
   
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
}



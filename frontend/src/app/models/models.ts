

 
import { Injectable } from "@angular/core";
@Injectable(
    {
        providedIn: 'root'
    }
)
export class Invoice{
    id!:number;
    amount! :number;
    due_on! :Date
    sell_price! :number
}
import { Component, OnInit } from '@angular/core';
import { Apollo } from "apollo-angular";
import gql from "graphql-tag";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
    title = 'BaldurClient';
    bob = ""

    constructor(private apollo: Apollo) {}

    ngOnInit() {
        this.apollo.query({
            query: gql`{ user(q: "1") { email } }`
        }).subscribe(result => {
            this.bob = result.data && result.data["user"]["email"]
        });
    }
}

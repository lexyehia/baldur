import { Component, OnInit } from '@angular/core';
import { Apollo } from "apollo-angular";
import { getUserEmail } from "../graphql"

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
    title = 'BaldurClient';
    bob = ""

    constructor(private apollo: Apollo) {}

    async ngOnInit() {
        const { data } = await this.apollo.query({ query: getUserEmail(1) }).toPromise();
        this.bob = data["user"]["email"];
    }
}

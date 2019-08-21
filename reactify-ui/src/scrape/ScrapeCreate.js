import React, {Component} from 'react'

import ScrapeForm from './ScrapeForm'

class ScrapeCreate extends Component {
    render() {
        return (
            <div>
                <h1>Scrape Yelp</h1>
                <ScrapeForm/>
                <br/>
                <div className="jumbotron jumbotron-fluid">
                    <div className="container">
                        <h1 className="display-4">Yelp Scraper Demo</h1>
                        <p className="lead">This is a demo of a simple scraper
                            I built to fetch yelp reviews.</p>
                        <p className="lead" id="enhance">Instructions:</p>
                            <ul className="lead" id="enhance">1. Find the business’s yelp page</ul>

                            <ul className="lead" id="enhance">2. Copy the url and paste it into the text
                                box</ul>
                         <p className="lead">
                            <i>Note: This demo currently only scrapes three
                                pages, to minimize database storage. </i>
                         </p>
                         <p className="lead">
                            A fully developed standalone web app is currently
                            under developed and will allow for the retrieval
                            and temporary storage of all reviews. </p>
                    </div>
                </div>
            </div>
        )
    }

}

export default ScrapeCreate
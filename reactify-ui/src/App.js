import React, { Component } from 'react';
import { BrowserRouter, Route, Switch} from 'react-router-dom'
import './App.css';


import Posts from './posts/Posts';
import PostDetail from './posts/PostDetail';
import PostCreate from './posts/PostCreate';

import ScrapeDetail from './scrape/ScrapeDetail';
import ScrapeCreate from './scrape/ScrapeCreate'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
          <Switch>
            <Route exact path='/posts/create' component={PostCreate}/>
            <Route exact path='/posts/:slug/edit' component={PostCreate}/>
            <Route exact path='/posts/' component={Posts}/>
            <Route exact path='/posts/:slug' component={PostDetail}/>
            <Route exact path='/scrape/' component={ScrapeCreate}/>
            <Route exact path='/scrape/results/:slug' component={ScrapeDetail}/>
            {/*<Route component={Posts}/>*/}
          </Switch>
      </BrowserRouter>
    );
  }
}

export default App;

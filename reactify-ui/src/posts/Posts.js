import React, {Component} from 'react';
import 'whatwg-fetch'
import cookie from 'react-cookies'
import {Link} from 'react-router-dom'
import PostInline from './PostInline'
import Button from 'react-bootstrap/Button';

class Posts extends Component {

    constructor(props) {
        super(props);
        this.togglePostListClass = this.togglePostListClass.bind(this);
        this.handleNewPost = this.handleNewPost.bind(this);
        this.loadMorePosts = this.loadMorePosts.bind(this);
        this.state = {
            posts: [],
            postsListClass: "card",
            next: null,
            previous: null,
            author: false,
            count: 0
        }
    }

    loadMorePosts() {
        const {next} = this.state;
        if (next !== null || next !== undefined) {
            this.loadPosts(next)
        }

    }

    loadPosts(nextEndpoint) {
        let endpoint = '/api/posts/';
        if (nextEndpoint !== undefined) {
            endpoint = nextEndpoint
        }
        let thisComp = this;
        let lookupOptions = {
            method: "GET",
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const csrfToken = cookie.load('csrftoken');
        if (csrfToken !== undefined) {
            lookupOptions['credentials'] = 'include';
            lookupOptions['headers']['X-CSRFToken'] = csrfToken
        }

        fetch(endpoint, lookupOptions)
            .then(function (response) {
                return response.json()
            }).then(function (responseData) {
            console.log(responseData);
            let currentPosts = thisComp.state.posts;
            // let newPosts = currentPosts.concat(responseData.results)
            // console.log(currentPosts)
            thisComp.setState({
                posts: thisComp.state.posts.concat(responseData.results),
                next: responseData.next,
                previous: responseData.previous,
                author: responseData.author,
                count: responseData.count
            })
        }).catch(function (error) {
            console.log("error", error)
        })
    }

    handleNewPost(postItemData) {
        // console.log(postItemData)
        let currentPosts = this.state.posts;
        currentPosts.unshift(postItemData); // unshift
        this.setState({
            posts: currentPosts
        })
    }


    togglePostListClass(event) {
        event.preventDefault();
        let currentListClass = this.state.postsListClass;
        if (currentListClass === "") {
            this.setState({
                postsListClass: "card",
            })
        } else {
            this.setState({
                postsListClass: "",
            })
        }

    }

    componentDidMount() {
        this.setState({
            posts: [],
            postsListClass: "card",
            next: null,
            previous: null,
            author: true,
            count: 0
        });
        this.loadPosts()
    }

    render() {
        const {posts} = this.state;
        const {postsListClass} = this.state;
        const {author} = this.state;
        const {next} = this.state;
        return (
            <div className="container-fluid">
                {/*<h1>*/}
                {/*    {author === true ?*/}
                {/*        <Link className='mr-2'*/}
                {/*              maintainScrollPosition={false}*/}
                {/*              to={{*/}
                {/*                  pathname: `/posts/create/`,*/}
                {/*                  state: {fromDashboard: false}*/}
                {/*              }}>Create Post</Link> : ""} <b/>*/}

                    {/*<Button onClick={this.togglePostListClass}>List View</Button>*/}
                {/*</h1>*/}
                <br/>
                    <div className="card-columns">
                        {posts.length > 0 ? posts.map((postItem, index) => {
                            return (
                                <PostInline post={postItem}
                                            elClass={postsListClass}/>
                                            )
                        }) : <p>No Posts Found</p>}
                        {next !== null ? <Button onClick={this.loadMorePosts}>Load
                            more</Button> : ''}
                    </div>
                </div>
        );
    }
}

export default Posts;
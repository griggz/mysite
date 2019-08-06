import React, {Component} from 'react'
import 'whatwg-fetch'
import cookie from 'react-cookies'
import {Link} from 'react-router-dom'
import twitLogo from './twitter.png'
import linkdLogo from './linkin.png'
import redditLogo from './reddit.svg'
import fbookLogo from './facebook.svg'
import PostForm from './PostForm'
import Moment from "react-moment";
import ReactMarkdown from "react-markdown";

class PostDetail extends Component {
    constructor(props) {
        super(props);
        this.handlePostItemUpdated = this.handlePostItemUpdated.bind(this);
        this.state = {
            slug: null,
            post: null,
            doneLoading: false,
        }
    }

    handlePostItemUpdated(postItemData) {
        this.setState({
            post: postItemData
        })
    }

    loadPost(slug) {
        const endpoint = `/api/posts/${slug}/`;
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
                if (response.status === 404) {
                    console.log('Page not found')
                }
                return response.json()
            }).then(function (responseData) {
            if (responseData.detail) {
                thisComp.setState({
                    doneLoading: true,
                    post: null
                })
            } else {
                thisComp.setState({
                    doneLoading: true,
                    post: responseData
                })
            }
        }).catch(function (error) {
            console.log("error", error)
        })
    }


    componentDidMount() {
        this.setState({
            slug: null,
            post: null
        });
        if (this.props.match) {
            const {slug} = this.props.match.params;
            this.setState({
                slug: slug,
                doneLoading: false
            });
            this.loadPost(slug)
        }
    }

    buildUrl() {
        const {post} = this.state;
        return (
         `https://vvayne.io/posts/${post.slug}` )
         }

    render() {
        const {doneLoading} = this.state;
        const {post} = this.state;
        const hrStyle = {
            display: 'block',
            height: '1px',
            border: 0,
            borderTop: '1px solid #ccc',
            margin: '1em 0',
            padding: '0',
            color: 'white'
        };
        return (
            <p>{(doneLoading === true) ? <div class="Main">
                {post === null ? "Not Found" :
                    <div className="container-fluid">
                        <div className='row'>
                            <div className='col-md-10'>
                                <h1 id='alt'>{post.title}</h1>
                                <h4 id='alt'>By {post.author.username}</h4>
                                <hr style={hrStyle}/>
                                <h4>
                                    <small
                                        className="publish_date"
                                        id='alt'> Published: <Moment
                                        fromNow
                                        ago>{post.timestamp}</Moment> ago&nbsp;
                                    </small>
                                </h4>
                                <hr style={hrStyle}/>
                                <img src={post.unsplash_url}
                                     class="rounded img-fluid"
                                     alt="sigil"/>
                                <hr style={hrStyle}/>
                                <small id='shareIconsContainer'>
                                    <a href={ `https://www.facebook.com/sharer/sharer.php?u=${this.buildUrl()}`}
                                       id='shareIcons'><img
                                        src={fbookLogo} alt="facebook"
                                    /></a> |&nbsp;
                                    <a href={ `https://twitter.com/home?status=${this.buildUrl()}`}
                                       id='shareIcons'><img
                                        src={twitLogo} alt="twitter"
                                    /></a> |&nbsp;
                                    <a href={ `https://www.linkedin.com/shareArticle?mini=true&url=${this.buildUrl()}&title=${post.title}&summary=${post.title}}&source=${this.buildUrl()}&`}
                                       id='shareIcons'><img
                                        src={linkdLogo} alt="linkdin"
                                    /></a> |&nbsp;
                                    <a href={` http://www.reddit.com/submit?url=${this.buildUrl()}&title=${post.title}&`}
                                       id='shareIcons'><img
                                        src={redditLogo} alt="reddit"
                                    /></a>
                                </small>
                                <p id="alt">
                                    <ReactMarkdown
                                        source={post.content}/>
                                </p>

                            </div>

                            <div className='col-md-2'>
                                <br/>
                            </div>
                        </div>
                    </div>
                }
            </div> : "Loading..."}</p>
        )
    }
}

export default PostDetail
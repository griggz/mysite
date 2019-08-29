import React, {Component} from 'react'
import 'whatwg-fetch'
import cookie from 'react-cookies'
import Moment from "react-moment";
import ReactMarkdown from "react-markdown";
import {
    FacebookIcon,
    LinkedinIcon,
    TwitterIcon,
    RedditIcon,
    InstapaperIcon,
    EmailIcon,
    FacebookShareButton,
    LinkedinShareButton,
    TwitterShareButton,
    RedditShareButton,
    InstapaperShareButton,
    EmailShareButton
} from 'react-share';
import {Link} from "react-router-dom";
import Button from "react-bootstrap/Button";

class PostDetail extends Component {
    constructor(props) {
        super(props);
        this.handlePostItemUpdated = this.handlePostItemUpdated.bind(this);
        this.state = {
            slug: null,
            post: null,
            doneLoading: false,
            owner: null
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
                    post: responseData,
                    owner: responseData.owner,
                });
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
            `https://vvayne.io/posts/${post.slug}`)
    }

    render() {
        const {doneLoading} = this.state;
        const {post} = this.state;
        const {owner} = this.state;
        console.log(post)

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
                    <div className='row'>
                        <div className='col-md-10'>
                            <h1 id='alt'>{post.title}</h1>
                            <h4 id='alt'>By {post.author.username}&nbsp;
                                {owner === true ?
                                    <Link className='mr-2'
                                          maintainScrollPosition={false}
                                          to={{pathname: `/posts/${post.slug}/edit`,
                                              state: {post: post}
                                          }}><Button variant="outline-light"
                                                     type="button" id="edit-button">Edit</Button>
                                    </Link> : ""} </h4>
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
                                <EmailShareButton url={this.buildUrl()}>
                                    <EmailIcon size={32} round={true}/>
                                </EmailShareButton>
                            </small>
                            <small id='shareIconsContainer'>
                                <FacebookShareButton url={this.buildUrl()}>
                                    <FacebookIcon size={32} round={true}/>
                                </FacebookShareButton>
                            </small>
                            <small id='shareIconsContainer'>
                                <TwitterShareButton url={this.buildUrl()}>
                                    <TwitterIcon size={32} round={true}/>
                                </TwitterShareButton>
                            </small>
                            <small id='shareIconsContainer'>
                                <LinkedinShareButton url={this.buildUrl()}>
                                    <LinkedinIcon size={32} round={true}/>
                                </LinkedinShareButton>
                            </small>
                            <small id='shareIconsContainer'>
                                <RedditShareButton url={this.buildUrl()}>
                                    <RedditIcon size={32} round={true}/>
                                </RedditShareButton>
                            </small>
                            <small id='shareIconsContainer'>
                                <InstapaperShareButton url={this.buildUrl()}>
                                    <InstapaperIcon size={32} round={true}/>
                                </InstapaperShareButton>
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
                }
            </div> : "Loading..."}</p>
        )
    }
}

export default PostDetail
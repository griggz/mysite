import React, {Component} from 'react'
import 'whatwg-fetch'
import cookie from 'react-cookies'
import moment from 'moment'
import ReactMarkdown from "react-markdown";
import {Redirect} from "react-router-dom";
import Button from "react-bootstrap/Button";

class PostForm extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleDraftChange = this.handleDraftChange.bind(this);
        this.clearForm = this.clearForm.bind(this);
        this.postTitleRef = React.createRef();
        this.postContentRef = React.createRef();
        this.postUnsplashRef = React.createRef();
        this.state = {
            draft: false,
            title: null,
            content: null,
            publish: null,
            post_image: null,
            redirect: false,
            redirectLink: null,
            errors: {},
        }
    }

    createPost(data) {
        const endpoint = '/api/posts/';
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;
        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(data),
                credentials: 'include'
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                thisComp.setState({redirectLink: `/posts/${responseData.slug}`});
                if (thisComp.props.newPostItemCreated) {
                    thisComp.props.newPostItemCreated(responseData)
                }
                thisComp.clearForm();
            }).catch(function (error) {
                console.log("error", error);
                alert("An error occurred, please try again later.")
            }).then(() => this.setState({redirect: true}));
        }

    }

    updatePost(data) {
        const {post} = this.props;
        const endpoint = `/api/posts/${post.slug}/`;
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;
        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: "PUT",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(data),
                credentials: 'include'
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                thisComp.setState({redirectLink: `/posts/${responseData.slug}`});
                // console.log(responseData)
                if (thisComp.props.postItemUpdated) {
                    thisComp.props.postItemUpdated(responseData)
                }

            }).catch(function (error) {
                console.log("error", error);
                alert("An error occurred, please try again later.")
            }).then(() => this.setState({redirect: true}));
        }

    }

    handleSubmit(event) {
        event.preventDefault();
        let data = this.state;

        const {post} = this.props;
        if (post !== undefined) {
            this.updatePost(data)
        } else {
            this.createPost(data)
        }

    }

    handleInputChange(event) {
        event.preventDefault();
        let key = event.target.name;
        let value = event.target.value;
        if (key === 'title') {
            if (value.length > 120) {
                alert("This title is too long")
            }
        }
        this.setState({
            [key]: value
        })
    }

    handleDraftChange(event) {
        this.setState({
            draft: !this.state.draft
        })
    }

    clearForm(event) {
        if (event) {
            event.preventDefault()
        }
        this.postCreateForm.reset();
        this.defaultState()
    }


    clearFormRefs() {
        this.postTitleRef.current = '';
        this.postContentRef.current = '';
        this.postUnsplashRef.current = ''
    }


    defaultState() {
        this.setState({
            draft: false,
            title: null,
            content: null,
            post_image: null,
            publish: moment(new Date()).format('YYYY-MM-DD'),
        });
    }

    componentDidMount() {
        const {post} = this.props;
        if (post !== undefined) {
            this.setState({
                draft: post.draft,
                title: post.title,
                content: post.content,
                post_image: post.post_image,
                publish: moment(post.publish).format('YYYY-MM-DD'),
            })
        } else {
            this.defaultState()
        }
        // this.postTitleRef.current.focus()
    }

    render() {
        const {publish} = this.state;
        const {title} = this.state;
        const {content} = this.state;
        const {post_image} = this.state;
        const {redirect} = this.state;
        const {redirectLink} = this.state;
        if (redirect) {
            return <Redirect to={redirectLink}/>;
        }
        return (
            <div>
                <h1>Create Post</h1>
                <form onSubmit={this.handleSubmit}
                      ref={(el) => this.postCreateForm = el}>
                    <div className='form-group' id='top-row-form'>
                        <label htmlFor='draft'>
                            <input type='checkbox'
                                   checked={this.state.draft}
                                   id='draft'
                                   name='draft'
                                   className='mr-2'
                                   onChange={this.handleDraftChange}/>
                        </label>
                        <Button variant="outline-light"
                                onClick={(event) => {
                                    event.preventDefault();
                                    this.handleDraftChange()
                                }}>Draft
                        </Button>
                        <label htmlFor='publish'>Publish Date</label>
                        <input
                            type='date'
                            id='publish'
                            name='publish'
                            className='form-control'
                            onChange={this.handleInputChange}
                            value={publish}
                            required='required'/>
                        <button type='submit' className='btn btn-primary'
                                id='create-submit'>Save
                        </button>
                    </div>
                    <div className='form-group'>
                        <input
                            type='text'
                            id='title'
                            name='title'
                            value={title}
                            className='form-control'
                            placeholder='Blog post title'
                            ref={this.postTitleRef}
                            onChange={this.handleInputChange}
                            required='required'/>
                    </div>
                    <div className='form-group'>
                        <label for='post_image'>
                            <small>Get your photo ID from <a
                                href="https://unsplash.com"
                                target="_blank">Unsplash.com</a>. Use this <a
                                href="http://quick.as/x3vycpgog"
                                target="_blank">guide</a> if you need help. Or,
                                if you want a random image, enter "random" to
                                pull random images from unsplash.
                            </small>
                        </label>
                        <input
                            type='text'
                            id='post_image'
                            name='post_image'
                            value={post_image}
                            className='form-control'
                            placeholder='post_image'
                            ref={this.postUnsplashRef}
                            onChange={this.handleInputChange}
                            required='required'/>
                    </div>
                    <div className='form-group'>
                        {/*<label for='content'>Content</label>*/}
                        <textarea
                            id='content'
                            ref={this.postContentRef}
                            name='content'
                            value={content}
                            className='form-control'
                            placeholder='Post content'
                            onChange={this.handleInputChange}
                            required='required'/>

                    </div>
                    <div className="preview">
                        <div className="preview-text">
                            <ReactMarkdown source={content}/>
                        </div>
                    </div>
                </form>
            </div>
        )
    }

}

export default PostForm
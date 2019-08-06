import React, {Component} from 'react';
import {Link} from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import Moment from 'react-moment';

class PostInline extends Component {

    render() {
        const {post} = this.props;
        const {elClass} = this.props;
        const showContent = elClass === 'card' ? 'd-block' : 'd-none';
        return (

            <div className={elClass}>
                <div className="card-body">
                    <img src={post.unsplash_url}
                         class="card-img-top"
                         alt={'sigil'}/>
                    <small class="image_source"><a
                        href='https://unsplash.com/photos/{post.unsplash_url}'
                        TARGET="_blank">Image Source</a></small>
                    <h1 class="title">
                        <Link maintainScrollPosition={false} to={{
                            pathname: `/posts/${post.slug}`,
                            state: {fromDashboard: false}
                        }}>{post.title}</Link></h1>
                    <h4>
                        <small
                            class="publish_date"> Published: <Moment
                            fromNow
                            ago>{post.timestamp}</Moment> ago
                        </small>
                    </h4>
                    {/*<h4>*/}
                    {/*    Author: {post.author.username}*/}
                    {/*</h4>*/}
                    <h4>
                        Read time: {post.read_time} min:
                    </h4>
                    <hr/>
                    <p className={showContent}>
                        <ReactMarkdown
                            source={post.content.slice(0,200).trim().concat('...' )} /><Link maintainScrollPosition={false} to={{
                            pathname: `/posts/${post.slug}`,
                            state: {fromDashboard: false}
                        }}>
                            <button className={`btn btn-primary`}>Read
                                More
                            </button></Link>
                    </p>
                </div>
            </div>
                );
                }
                }

                export default PostInline

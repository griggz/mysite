(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{104:function(e,t,a){e.exports=a(274)},109:function(e,t,a){},110:function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},111:function(e,t,a){},201:function(e,t,a){e.exports=a.p+"static/media/twitter.bdda731e.png"},202:function(e,t,a){e.exports=a.p+"static/media/linkin.34ca7885.png"},203:function(e,t,a){e.exports=a.p+"static/media/reddit.12eae182.svg"},204:function(e,t,a){e.exports=a.p+"static/media/facebook.a75369d0.svg"},251:function(e,t){},274:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),s=a(96),l=a.n(s),o=(a(109),a(2)),i=a(3),c=a(6),u=a(4),d=a(5),m=a(290),h=a(293),p=a(292),f=(a(110),a(111),a(7)),b=(a(32),a(14)),v=a.n(b),g=a(277),E=a(46),y=a.n(E),k=a(47),C=a.n(k),j=function(e){function t(){return Object(o.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props.post,t=this.props.elClass,a="card"===t?"d-block":"d-none";return r.a.createElement("div",{className:t},r.a.createElement("div",{className:"card-body"},r.a.createElement("img",{src:e.unsplash_url,class:"card-img-top",alt:"sigil"}),r.a.createElement("small",{class:"image_source"},r.a.createElement("a",{href:"https://unsplash.com/photos/{post.unsplash_url}",TARGET:"_blank"},"Image Source")),r.a.createElement("h1",{class:"title"},r.a.createElement(g.a,{maintainScrollPosition:!1,to:{pathname:"/posts/".concat(e.slug),state:{fromDashboard:!1}}},e.title),!0===e.draft?r.a.createElement("small",{className:"draft"}," Draft"):""),r.a.createElement("h4",null,r.a.createElement("small",{class:"publish_date"}," Published: ",r.a.createElement(C.a,{fromNow:!0,ago:!0},e.timestamp)," ago")),r.a.createElement("h4",null,"Read time: ",e.read_time," min:"),r.a.createElement("hr",null),r.a.createElement("p",{className:a},r.a.createElement(y.a,{source:e.content.slice(0,200).trim().concat("...")}),r.a.createElement(g.a,{maintainScrollPosition:!1,to:{pathname:"/posts/".concat(e.slug),state:{fromDashboard:!1}}},r.a.createElement("button",{className:"btn btn-primary"},"Read More")))))}}]),t}(n.Component),O=a(37),S=a.n(O),N=function(e){function t(e){var a;return Object(o.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).togglePostListClass=a.togglePostListClass.bind(Object(f.a)(a)),a.handleNewPost=a.handleNewPost.bind(Object(f.a)(a)),a.loadMorePosts=a.loadMorePosts.bind(Object(f.a)(a)),a.state={posts:[],postsPublic:[],postsListClass:"card",previous:null,author:!1,draft:null,count:0},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"loadMorePosts",value:function(){var e=this.state.next;null===e&&void 0===e||this.loadPosts(e)}},{key:"loadPosts",value:function(e){var t="/api/posts/";void 0!==e&&(t=e);var a=this,n={method:"GET",headers:{"Content-Type":"application/json"}},r=v.a.load("csrftoken");void 0!==r&&(n.credentials="include",n.headers["X-CSRFToken"]=r),fetch(t,n).then(function(e){return e.json()}).then(function(e){var t=e.results.filter(function(e){return!1===e.draft});a.setState({posts:a.state.posts.concat(e.results),postsPublic:a.state.postsPublic.concat(t),next:e.next,previous:e.previous,staff:e.staff,draft:e.draft,count:e.count})}).catch(function(e){console.log("error",e)})}},{key:"handlePosts",value:function(e){var t=e.filter(function(e){return!1===e.draft});this.setState({postsPublic:t})}},{key:"handleNewPost",value:function(e){var t=this.state.posts;t.unshift(e),this.setState({posts:t})}},{key:"togglePostListClass",value:function(e){e.preventDefault(),""===this.state.postsListClass?this.setState({postsListClass:"card"}):this.setState({postsListClass:""})}},{key:"componentDidMount",value:function(){this.setState({posts:[],postsListClass:"card",next:null,previous:null,count:0}),this.loadPosts()}},{key:"render",value:function(){var e=this.state.posts,t=this.state.postsPublic,a=this.state.postsListClass,n=this.state.staff,s=this.state.next;return r.a.createElement("div",{className:"container-fluid"},r.a.createElement("br",null),!0===n?r.a.createElement("div",{className:"card-columns"},e.length>0?e.map(function(e,t){return r.a.createElement(j,{post:e,elClass:a})}):r.a.createElement("p",null,"No Posts Found")):r.a.createElement("div",{className:"card-columns"},e.length>0?t.map(function(e,t){return r.a.createElement(j,{post:e,elClass:a})}):r.a.createElement("p",null,"No Posts Found")),r.a.createElement("div",{className:"d-flex flex-column text-center"},null!==s?r.a.createElement(S.a,{variant:"outline-light",onClick:this.loadMorePosts},"Load more"):""),r.a.createElement("br",null))}}]),t}(n.Component),P=(a(201),a(202),a(203),a(204),a(49)),w=a(48),x=a.n(w),F=function(e){function t(e){var a;return Object(o.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).handleSubmit=a.handleSubmit.bind(Object(f.a)(a)),a.handleInputChange=a.handleInputChange.bind(Object(f.a)(a)),a.handleDraftChange=a.handleDraftChange.bind(Object(f.a)(a)),a.clearForm=a.clearForm.bind(Object(f.a)(a)),a.postTitleRef=r.a.createRef(),a.postContentRef=r.a.createRef(),a.state={draft:!1,title:null,content:null,publish:null,errors:{}},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"createPost",value:function(e){var t=v.a.load("csrftoken"),a=this;if(void 0!==t){var n={method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":t},body:JSON.stringify(e),credentials:"include"};fetch("/api/posts/",n).then(function(e){return e.json()}).then(function(e){console.log(e),a.props.newPostItemCreated&&a.props.newPostItemCreated(e),a.clearForm()}).catch(function(e){console.log("error",e),alert("An error occured, please try again later.")})}}},{key:"updatePost",value:function(e){var t=this.props.post,a="/api/posts/".concat(t.slug,"/"),n=v.a.load("csrftoken"),r=this;if(void 0!==n){var s={method:"PUT",headers:{"Content-Type":"application/json","X-CSRFToken":n},body:JSON.stringify(e),credentials:"include"};fetch(a,s).then(function(e){return e.json()}).then(function(e){r.props.postItemUpdated&&r.props.postItemUpdated(e)}).catch(function(e){console.log("error",e),alert("An error occured, please try again later.")})}}},{key:"handleSubmit",value:function(e){e.preventDefault();var t=this.state;void 0!==this.props.post?this.updatePost(t):this.createPost(t)}},{key:"handleInputChange",value:function(e){e.preventDefault();var t=e.target.name,a=e.target.value;"title"===t&&a.length>120&&alert("This title is too long"),this.setState(Object(P.a)({},t,a))}},{key:"handleDraftChange",value:function(e){this.setState({draft:!this.state.draft})}},{key:"clearForm",value:function(e){e&&e.preventDefault(),this.postCreateForm.reset(),this.defaultState()}},{key:"clearFormRefs",value:function(){this.postTitleRef.current="",this.postContentRef.current=""}},{key:"defaultState",value:function(){this.setState({draft:!1,title:null,content:null,publish:x()(new Date).format("YYYY-MM-DD")})}},{key:"componentDidMount",value:function(){var e=this.props.post;void 0!==e?this.setState({draft:e.draft,title:e.title,content:e.content,publish:x()(e.publish).format("YYYY-MM-DD")}):this.defaultState()}},{key:"render",value:function(){var e=this,t=this.state.publish,a=this.state.title,n=this.state.content;this.props.post;return r.a.createElement("form",{onSubmit:this.handleSubmit,ref:function(t){return e.postCreateForm=t}},r.a.createElement("div",{className:"form-group"},r.a.createElement("label",{for:"title"},"Post title"),r.a.createElement("input",{type:"text",id:"title",name:"title",value:a,className:"form-control",placeholder:"Blog post title",ref:this.postTitleRef,onChange:this.handleInputChange,required:"required"})),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",{for:"content"},"Content"),r.a.createElement("textarea",{id:"content",ref:this.postContentRef,name:"content",value:n,className:"form-control",placeholder:"Post content",onChange:this.handleInputChange,required:"required"})),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",{for:"draft"},r.a.createElement("input",{type:"checkbox",checked:this.state.draft,id:"draft",name:"draft",className:"mr-2",onChange:this.handleDraftChange}),"Draft "),r.a.createElement("button",{onClick:function(t){t.preventDefault(),e.handleDraftChange()}},"Toggle Draft")),r.a.createElement("div",{className:"form-group"},r.a.createElement("label",{for:"publish"},"Publish Date"),r.a.createElement("input",{type:"date",id:"publish",name:"publish",className:"form-control",onChange:this.handleInputChange,value:t,required:"required"})),r.a.createElement("button",{type:"submit",className:"btn btn-primary"},"Save"),r.a.createElement("button",{className:"btn btn-secondary",onClick:this.clearForm},"Clear"))}}]),t}(n.Component),D=a(278),T=a(279),I=a(280),L=a(281),R=a(282),M=a(283),U=a(284),Y=a(285),_=a(286),q=a(287),z=a(288),X=a(289),A=function(e){function t(e){var a;return Object(o.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).handlePostItemUpdated=a.handlePostItemUpdated.bind(Object(f.a)(a)),a.state={slug:null,post:null,doneLoading:!1},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"handlePostItemUpdated",value:function(e){this.setState({post:e})}},{key:"loadPost",value:function(e){var t="/api/posts/".concat(e,"/"),a=this,n={method:"GET",headers:{"Content-Type":"application/json"}},r=v.a.load("csrftoken");void 0!==r&&(n.credentials="include",n.headers["X-CSRFToken"]=r),fetch(t,n).then(function(e){return 404===e.status&&console.log("Page not found"),e.json()}).then(function(e){e.detail?a.setState({doneLoading:!0,post:null}):a.setState({doneLoading:!0,post:e})}).catch(function(e){console.log("error",e)})}},{key:"componentDidMount",value:function(){if(this.setState({slug:null,post:null}),this.props.match){var e=this.props.match.params.slug;this.setState({slug:e,doneLoading:!1}),this.loadPost(e)}}},{key:"buildUrl",value:function(){var e=this.state.post;return"https://vvayne.io/posts/".concat(e.slug)}},{key:"render",value:function(){var e=this.state.doneLoading,t=this.state.post,a={display:"block",height:"1px",border:0,borderTop:"1px solid #ccc",margin:"1em 0",padding:"0",color:"white"};return r.a.createElement("p",null,!0===e?r.a.createElement("div",{class:"Main"},null===t?"Not Found":r.a.createElement("div",{className:"container-fluid"},r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col-md-10"},r.a.createElement("h1",{id:"alt"},t.title),r.a.createElement("h4",{id:"alt"},"By ",t.author.username),r.a.createElement("hr",{style:a}),r.a.createElement("h4",null,r.a.createElement("small",{className:"publish_date",id:"alt"}," Published: ",r.a.createElement(C.a,{fromNow:!0,ago:!0},t.timestamp)," ago\xa0")),r.a.createElement("hr",{style:a}),r.a.createElement("img",{src:t.unsplash_url,class:"rounded img-fluid",alt:"sigil"}),r.a.createElement("hr",{style:a}),r.a.createElement("small",{id:"shareIconsContainer"},r.a.createElement(D.a,{url:this.buildUrl()},r.a.createElement(T.a,{size:32,round:!0}))),r.a.createElement("small",{id:"shareIconsContainer"},r.a.createElement(I.a,{url:this.buildUrl()},r.a.createElement(L.a,{size:32,round:!0}))),r.a.createElement("small",{id:"shareIconsContainer"},r.a.createElement(R.a,{url:this.buildUrl()},r.a.createElement(M.a,{size:32,round:!0}))),r.a.createElement("small",{id:"shareIconsContainer"},r.a.createElement(U.a,{url:this.buildUrl()},r.a.createElement(Y.a,{size:32,round:!0}))),r.a.createElement("small",{id:"shareIconsContainer"},r.a.createElement(_.a,{url:this.buildUrl()},r.a.createElement(q.a,{size:32,round:!0}))),r.a.createElement("small",{id:"shareIconsContainer"},r.a.createElement(z.a,{url:this.buildUrl()},r.a.createElement(X.a,{size:32,round:!0}))),r.a.createElement("p",{id:"alt"},r.a.createElement(y.a,{source:t.content}))),r.a.createElement("div",{className:"col-md-2"},r.a.createElement("br",null))))):"Loading...")}}]),t}(n.Component),B=function(e){function t(){return Object(o.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement("h1",null,"Create Post"),r.a.createElement(F,null))}}]),t}(n.Component),J=function(e){function t(){return Object(o.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props.reviews;return r.a.createElement("div",{className:"col-lg-12"},r.a.createElement("td",{className:"dash h5"},r.a.createElement("b",null,e.author)," |"),r.a.createElement("td",{className:"dash h5"},r.a.createElement("b",null,e.date)," |"),r.a.createElement("td",{className:"dash h5"},r.a.createElement("b",null,e.rating)),r.a.createElement("p",{className:"dash"},e.review),r.a.createElement("hr",{style:{display:"block",height:"1px",border:0,borderTop:"1px solid #ccc",margin:"1em 0",padding:"0",color:"white"}}))}}]),t}(n.Component),G=(a(251),a(291)),W=a(102),$=a.n(W),H=function(e){function t(e){var a;return Object(o.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).state={slug:null,scrape:null,doneLoading:!1,visible:25,words:null},a.loadMore=a.loadMore.bind(Object(f.a)(a)),a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"loadMore",value:function(){this.setState(function(e){return{visible:e.visible+25}})}},{key:"handlePostItemUpdated",value:function(e){this.setState({scrape:e})}},{key:"loadReviews",value:function(e){var t="/api/scrape/".concat(e,"/"),a=this,n={method:"GET",headers:{"Content-Type":"application/json"}},r=v.a.load("csrftoken");void 0!==r&&(n.credentials="include",n.headers["X-CSRFToken"]=r),fetch(t,n).then(function(e){return 404===e.status&&console.log("Page not found"),e.json()}).then(function(e){e.detail?a.setState({doneLoading:!0,scrape:null}):a.setState({doneLoading:!0,scrape:e})}).catch(function(e){console.log("error",e)})}},{key:"componentDidMount",value:function(){if(this.setState({slug:null}),this.props.match){var e=this.props.match.params.slug;this.setState({slug:e,doneLoading:!1}),this.loadReviews(e)}}},{key:"buildUrl",value:function(){var e=this.state.scrape;return"https://vvayne.io/scrape/results/".concat(e.slug)}},{key:"buildFileName",value:function(){var e=this.state.scrape;return"".concat(e.business_name,".csv")}},{key:"render",value:function(){var e=this,t=this.state.doneLoading,a=this.state.scrape;return r.a.createElement("p",null,!0===t?r.a.createElement("div",{class:"Main"},null===a?"No Reviews Found...In order to use this\nscraper you must be a registered user and\nlogged in. If you are logged in and receiving\nthis error, please confirm that the business\nyou are attempting to scrape has reviews.":r.a.createElement("div",{className:"container-fluid"},r.a.createElement(g.a,{maintainScrollPosition:!1,to:{pathname:"/scrape",state:{fromDashboard:!1}}},r.a.createElement("button",{className:"btn btn-primary"},"New Scrape")),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("h1",null,a.business_name),r.a.createElement(S.a,{variant:"secondary",onClick:function(){return $()(a.reviews,e.buildFileName())}},"Download Data"),r.a.createElement("hr",{style:{display:"block",height:"1px",border:0,borderTop:"1px solid #ccc",margin:"1em 0",padding:"0",color:"white"}}),a.reviews.length>0?a.reviews.slice(0,this.state.visible).map(function(e,t){return r.a.createElement("div",{className:"row",key:t},r.a.createElement(J,{reviews:e}))}):r.a.createElement("p",null,"No Reviews Found"),this.state.visible<a.reviews.length&&r.a.createElement("div",{className:"d-flex flex-column text-center"},r.a.createElement(S.a,{onClick:this.loadMore,variant:"outline-light",type:"button",className:"load-more"},"Load more")))):r.a.createElement("div",{class:"spinner-border",role:"status"},r.a.createElement("span",{class:"sr-only"},"Loading...")))}}],[{key:"routeChange",value:function(){return r.a.createElement(G.a,{to:"/scrape/create"})}}]),t}(n.Component),K=a(103),Q=a.n(K),V=function(e){function t(e){var a;return Object(o.a)(this,t),(a=Object(c.a)(this,Object(u.a)(t).call(this,e))).handleSubmit=a.handleSubmit.bind(Object(f.a)(a)),a.handleInputChange=a.handleInputChange.bind(Object(f.a)(a)),a.clearForm=a.clearForm.bind(Object(f.a)(a)),a.scrapeLinkRef=r.a.createRef(),a.state={link:null,redirect:!1,slug:null,redirectLink:null,scraping:null,errors:{}},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"createScrape",value:function(e){var t=this,a=v.a.load("csrftoken"),n=this;if(void 0!==a){var r={method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":a},body:JSON.stringify(e),credentials:"include"};fetch("/api/scrape/",r).then(function(e){return e.json()}).then(function(e){n.setState({redirectLink:"/scrape/results/".concat(e.slug),scraping:null}),n.clearForm()}).catch(function(e){console.log("error",e),alert("An error occurred, please try again later.")}).then(function(){return t.setState({redirect:!0})})}}},{key:"handleSubmit",value:function(e){e.preventDefault();var t=this.state;void 0===this.props.scrape?(this.setState({scraping:!0}),this.createScrape(t)):this.clearFormRefs()}},{key:"handleInputChange",value:function(e){e.preventDefault();var t=e.target.name,a=e.target.value;"link"===t&&a.length>120&&alert("This link is too long"),this.setState(Object(P.a)({},t,a))}},{key:"clearForm",value:function(e){e&&e.preventDefault(),this.scrapeCreateForm.reset(),this.defaultState()}},{key:"clearFormRefs",value:function(){this.scrapeLinkRef.current=""}},{key:"defaultState",value:function(){this.setState({link:null})}},{key:"componentDidMount",value:function(){var e=this.props.scrape;void 0!==e?this.setState({link:e.link}):this.defaultState()}},{key:"render",value:function(){var e=this,t=this.state.link,a=this.state.redirect,n=this.state.redirectLink;return this.state.scraping?r.a.createElement("div",{id:"react-loader"},r.a.createElement(Q.a,{type:"Puff",color:"#00BFFF",height:"200",width:"200"})," ...scraping ",t):a?r.a.createElement(G.a,{to:n}):r.a.createElement("form",{onSubmit:this.handleSubmit,ref:function(t){return e.scrapeCreateForm=t}},r.a.createElement("div",{className:"form-group"},r.a.createElement("input",{type:"text",id:"link",name:"link",value:t,className:"form-control",placeholder:"Yelp Link",ref:this.scrapeLinkRef,onChange:this.handleInputChange,required:"required"})),r.a.createElement("button",{type:"submit",className:"btn btn-primary"},"Scrape"),"\xa0",r.a.createElement("button",{className:"btn btn-secondary",onClick:this.clearForm},"Clear"))}}]),t}(n.Component),Z=function(e){function t(){return Object(o.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement("h1",null,"Scrape Yelp"),r.a.createElement(V,null),r.a.createElement("br",null),r.a.createElement("div",{className:"jumbotron jumbotron-fluid"},r.a.createElement("div",{className:"container"},r.a.createElement("h1",{className:"display-4"},"Yelp Scraper Demo"),r.a.createElement("p",{className:"lead"},"This is a demo of a simple scraper I built to fetch yelp reviews."),r.a.createElement("p",{className:"lead",id:"enhance"},"Instructions:"),r.a.createElement("ul",{className:"lead",id:"enhance"},"1. Find a business\u2019s yelp page"),r.a.createElement("ul",{className:"lead",id:"enhance"},"2. Copy the url and paste it into the text box"),r.a.createElement("p",{className:"lead"},r.a.createElement("i",null,"Note: This demo currently only scrapes up to three pages, to minimize database storage. ")),r.a.createElement("p",{className:"lead"},"A fully developed standalone web app is currently under development and will allow for the retrieval and temporary storage of all reviews. "))))}}]),t}(n.Component),ee=function(e){function t(){return Object(o.a)(this,t),Object(c.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(m.a,null,r.a.createElement(h.a,null,r.a.createElement(p.a,{exact:!0,path:"/posts/create",component:B}),r.a.createElement(p.a,{exact:!0,path:"/posts/",component:N}),r.a.createElement(p.a,{exact:!0,path:"/posts/:slug",component:A}),r.a.createElement(p.a,{exact:!0,path:"/scrape/",component:Z}),r.a.createElement(p.a,{exact:!0,path:"/scrape/results/:slug",component:H})))}}]),t}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(r.a.createElement(ee,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[104,1,2]]]);
//# sourceMappingURL=main.24ba4c69.chunk.js.map
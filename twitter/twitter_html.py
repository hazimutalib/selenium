import streamlit as st
from PIL import Image

def kpi_box_html(total_tweets, total_comments, total_user):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card red-gradient ">
            <span class="card-value">{:,}</span>
            <span class="card-text">Total Posts</span>
        </div>
        <div class="kpi-card red-gradient ">
            <span class="card-value">{:,}</span>
            <span class="card-text">Total Comments</span>
        </div>
        <div class="kpi-card red-gradient ">
            <span class="card-value">{:,}</span>
            <span class="card-text">Total Username</span>
        </div>
    </div>
    """.format(total_tweets, total_comments, total_user), unsafe_allow_html=True)



def tweets_html(avatar, nikcname, username, tweets, img1, img2, img3, img4, numberOfComments, numberOfRetweets, numberOfLikes, numberOfViews):

  lol ="""
    <div style = "width:450px;" >
      <div class="tweet-wrap" >
        <div class="tweet-header" style = "font-size: 0.1rem !important;">
          <img src="{}" alt="" class="avator">
          <div class="tweet-header-info" style = "font-size: 0.9rem;">
            {} <span>{}</span><span>. Jun 27</span>
            <p>{}</p>
          </div>
        </div>
      <div class="tweet-img-wrap"  style = "height:150px;">
        <a href = "{}"><img src="{}" alt="" class="tweet-img" style = "height:60%;"></a>
        <a href = "{}"><img src="{}" alt="" class="tweet-img" style = "height:60%;"></a>
        <a href = "{}"><img src="{}" alt="" class="tweet-img" style = "height:60%;"></a>
        <a href = "{}"><img src="{}" alt="" class="tweet-img" style = "height:60%;"></a>
      </div>
      <div class="tweet-info-counts">
        <div class="comments">
          <svg class="feather feather-message-circle sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
          <div class="comment-count">{}</div>
        </div>
        <div class="retweets">
          <svg class="feather feather-repeat sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path></svg>
          <div class="retweet-count">{}</div>
        </div>
        <div class="likes">
          <svg class="feather feather-heart sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
          <div class="likes-count">{} </div>
        </div>
        <div class="views">
          <svg class="feather feather-heart sc-dnqmqq jxshSx" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.004-10h2L6 21H4zm9.248 0v-7h2v7h-2z"></path></svg>
          <div class="views-count">{}</div>
        </div>
    </div>
    """.format(avatar, nikcname, username, tweets, img1, img1, img2, img2, img3, img3, img4, img4, numberOfComments, numberOfRetweets, numberOfLikes, numberOfViews)
  return lol



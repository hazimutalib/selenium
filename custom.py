import streamlit as st
from PIL import Image

def body_css():
    st.markdown(""" 
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open Sans">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}
    </style>
    """, unsafe_allow_html=True,)

def kpi_box_css():
    st.markdown("""
    <style>
    .icon {  
    float: right;
    font-size:500%;
    position: absolute;
    top:0rem;
    right:-0.3rem;
    opacity: .16;
    }


    #container
    {
    display: flex;
    }

    .grey-dark
    {
    background: #495057;
    color: #efefef;
    }

    .red-gradient {
    background: linear-gradient(180deg, rgba(0, 4, 40,0.8) 0%, rgba(0, 78, 146,0.8) 80%);
    color: #fff;
    }
    .red {
    background: #a83b3b;
    color: #fff;
    }


    .purple
    {
    background: #886ab5;
    color: #fff;
    }

    .orange {
    background: #ffc241;
    color: #fff;
    }

    .kpi-card
    {
    overflow: hidden;
    position: relative;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.75);;
    display: inline-block;
    float: left;
    padding: 1em;
    border-radius: 0.3em;
    font-family: sans-serif;  
    width: 180px;
    min-width: 180px;
    margin-right: 0em;
    margin-bottom: 30px;
    }

    .card-value {
    display: block;
    font-size: 200%;  
    font-weight: bolder;
    }

    .card-text {
    display:block;
    font-size: 70%;
    padding-left: 0.2em;
    }
    .lol {
    justify-content : space-around;
    }
    </style>
    """, unsafe_allow_html=True)

def tiktok_comments_css():
    st.markdown("""
    <style>
    .tiktok-1mf23fd-DivContentContainer {
        flex: 1 1 auto;
    }


    .tiktok-16r0vzi-DivCommentItemContainer {
        margin-bottom: 16px;
    }
    .tiktok-1kimton-DivCommentContentContainer {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        margin-bottom: 16px;
        position: relative;
    }
    .tiktok-cwmrys-StyledUserLinkAvatar {
        margin-right: 12px;
    }

    .tiktok-tuohvl-SpanAvatarContainer {
        display: inline-block;
        box-sizing: border-box;
        margin: 0px;
        padding: 0px;
        font-feature-settings: "tnum";
        position: relative;
        overflow: hidden;
        color: rgb(255, 255, 255);
        white-space: nowrap;
        text-align: center;
        vertical-align: middle;
        line-height: 32px;
        border-radius: 50%;
        background-color: rgba(136, 136, 136, 0.5);
    }

    .tiktok-1zpj2q-ImgAvatar {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }


    .tiktok-bhsg9d-StyledUserLinkName:hover, .tiktok-bhsg9d-StyledUserLinkName:active, .tiktok-bhsg9d-StyledUserLinkName:link {
        text-decoration: none;
    }
    .tiktok-bhsg9d-StyledUserLinkName {
        font-family: SofiaPro, Arial, Tahoma, PingFangSC, sans-serif;
        font-weight: 700;
        font-size: 18px;
        line-height: 25px;
    }

    .tiktok-mfqbp1-SpanUserNameText {
        font-family: ProximaNova, Arial, Tahoma, PingFangSC, sans-serif;
        font-size: 13px;
        color: #000000;
    }

    .tiktok-q9aj5z-PCommentText {
        font-size: 14px;
        line-height: 22px;
        white-space: pre-line;
        word-break: break-word;
        margin-bottom: 6px;
        margin-top: -20px;
    }

    .tiktok-1wmf4bu-PCommentSubContent {
        color: rgba(22, 24, 35, 0.5);
        font-size: 14px;
        line-height: 20px;
        margin-bottom: -16px;
    }

    .tiktok-nqnosi-SpanReplyButton {
        cursor: pointer;
        color: rgba(22, 24, 35, 0.5);
        font-weight: 400;
        margin-left: 24px;
    }

    .tiktok-mnluvt-DivActionContainer {
        margin-left: 18px;
        padding-right: 2px;
        width: 24px;
        flex: 0 0 24px;
        padding-top: 24px;
        display: flex;
        flex-direction: column;
        -webkit-box-align: center;
        align-items: center;
    }

    .tiktok-5g6iif-DivMoreContainer {
        position: relative;
        display: none;
    }
    .tiktok-fzlfzu-StyledMoreIcon {
        width: 24px;
        height: 24px;
        cursor: pointer;
        display: block;
    }

    .tiktok-1wyxwrs-DivLikeWrapper {
        color: rgba(22, 24, 35, 0.5);
        font-size: 12px;
        line-height: 17px;
        width: 20px;
        display: flex;
        flex-direction: column;
        -webkit-box-align: center;
        align-items: center;
        cursor: pointer;
    }

    .tiktok-1k32hld-SpanCount {
        font-size: 12px;
        line-height: 17px;
        margin-left: 4px;
    }

    .tiktok-zn6r1p-DivReplyContainer {
        padding-left: 52px;
    }

    .tiktok-1for4nf-DivReplyActionContainer {
        display: flex;
        flex-direction: row;
        -webkit-box-pack: justify;
        justify-content: space-between;
        position: relative;
    }
    .tiktok-1qqecn-PReplyActionText {
        color: rgba(22, 24, 35, 0.5);
        font-weight: 600;
        font-size: 12px;
        line-height: 20px;
        cursor: pointer;
    }

    </style>
    """, unsafe_allow_html=True,)

def tiktok_video_css():
    st.markdown(""" 
    <style>
    .tiktok-u7bnsh-DivItemContainer {
        margin-right: 14px;
        margin-left: 0%;
        width: 147px;
        margin-bottom: 16px;
        cursor: pointer;
        height: 300px;
    }
    .tiktok-1ys5eyp-DivCoverContainer {
        width: 80%;
        height: 150px;
        position: relative;
        border-radius: 8px;;
        overflow: hidden;

    }

    .tiktok-10vhom9-DivAuthor {
        color: rgba(22, 24, 35, 0.75);
        font-size: 12px;
        line-height: 16px;
        margin-bottom: 4px;
        display: flex;
        -webkit-box-align: center;
        align-items: center;
    }

    .tiktok-1gr26ha-DivOtherInfo {
        display: flex;
        height: 16px;
        color: rgba(22, 24, 35, 0.75);
        -webkit-box-align: center;
        align-items: center;
        font-size: 12px;
        margin-bottom: 30px;
    }

    .tiktok-m86b9p-ImgCover {
        width: 100%;
        height: 100%;
        object-fit: cover;
        background: rgba(22, 24, 35, 0.06);
    }

    .tiktok-1vcf1yi-DivTitle {
        color: rgb(22, 24, 35);
        font-weight: 700;
        display: -webkit-box;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        margin-bottom: 4px;
        word-break: break-word;
    }

    .tiktok-1s16qmh-SpanUniqueId {
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }

    .tiktok-1fai8zo-DivDate {
        margin-right: 8px;
    }
    </style>
    """, unsafe_allow_html=True,)

def kpi_box(total_videos, total_comments, total_user):
    st.markdown("""
    <div id="container"  class = "lol" >
        <div class="kpi-card red-gradient ">
            <span class="card-value">{:,}</span>
            <span class="card-text">Total Videos</span>
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
    """.format(total_videos, total_comments, total_user), unsafe_allow_html=True)

def tiktok_video_html(tiktok_link, tiktok_image, tiktok_caption, tiktok_creator, posted_date, tiktok_views, tiktok_likes):
    lol = """ 
    <div class="tiktok-u7bnsh-DivItemContainer e1ymawm01">
        <div class="tiktok-1ys5eyp-DivCoverContainer e1ymawm02">
            <a href = "{}"> 
            <img src={} class="tiktok-m86b9p-ImgCover e1ymawm04">
            </a>
            <div class="tiktok-i5lz20-DivDuration e1ymawm05">00:10</div>
        </div>
        <div class="tiktok-1vcf1yi-DivTitle e1ymawm06">{}</div>
        <div class="tiktok-10vhom9-DivAuthor e1ymawm07">
            <span class="tiktok-1s16qmh-SpanUniqueId e1ymawm08">{}</span>
        </div>
        <div class="tiktok-10vhom9-DivAuthor e1ymawm07">
            <span class="tiktok-1s16qmh-SpanUniqueId e1ymawm08">{}</span>
        </div>
        <div class="tiktok-1gr26ha-DivOtherInfo e1ymawm09">
            <svg class="like-icon tiktok-b82ygf-StyledPlay etrd4pu9" width="16" data-e2e="" height="16" viewBox="0 0 48 48" fill="rgba(22, 24, 35, 0.75)" color="rgba(22, 24, 35, 0.75)" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M16 10.554V37.4459L38.1463 24L16 10.554ZM12 8.77702C12 6.43812 14.5577 4.99881 16.5569 6.21266L41.6301 21.4356C43.5542 22.6038 43.5542 25.3962 41.6301 26.5644L16.5569 41.7873C14.5577 43.0012 12 41.5619 12 39.223V8.77702Z"></path></svg>
            <div class="tiktok-1fai8zo-DivDate e1ymawm010">{}</div>
            <svg class="tiktok-1490buc-StyledHeart e1ymawm011" width="16" data-e2e="" height="16" viewBox="0 0 48 48" fill="currentcolor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M24 9.01703C19.0025 3.74266 11.4674 3.736 6.67302 8.56049C1.77566 13.4886 1.77566 21.4735 6.67302 26.4016L22.5814 42.4098C22.9568 42.7876 23.4674 43 24 43C24.5326 43 25.0432 42.7876 25.4186 42.4098L41.327 26.4016C46.2243 21.4735 46.2243 13.4886 41.327 8.56049C36.5326 3.736 28.9975 3.74266 24 9.01703ZM21.4938 12.2118C17.9849 8.07195 12.7825 8.08727 9.51028 11.3801C6.16324 14.7481 6.16324 20.214 9.51028 23.582L24 38.1627L38.4897 23.582C41.8368 20.214 41.8368 14.7481 38.4897 11.3801C35.2175 8.08727 30.0151 8.07195 26.5062 12.2118L26.455 12.2722L25.4186 13.3151C25.0432 13.6929 24.5326 13.9053 24 13.9053C23.4674 13.9053 22.9568 13.6929 22.5814 13.3151L21.545 12.2722L21.4938 12.2118Z"></path>
            </svg>{}
        </div>
    </div>
        """.format(tiktok_link, tiktok_image, tiktok_caption, tiktok_creator, posted_date, tiktok_views, tiktok_likes)
    
    return lol


def tiktok_comments_html_test():
    lol ="""
<div class="tiktok-16r0vzi-DivCommentItemContainer eo72wou0">
  <div id="7088335299323446017" class="tiktok-1kimton-DivCommentContentContainer e1g2efjf0">
    <a data-e2e="comment-avatar-1" class="tiktok-cwmrys-StyledUserLinkAvatar e1g2efjf5" href="/@mrsyanjun2408" style="flex: 0 0 40px;">
      <span shape="circle" data-e2e="" class="tiktok-tuohvl-SpanAvatarContainer e1e9er4e0" style="width: 40px; height: 40px;">
        <img loading="lazy" src="https://p16-sign-va.tiktokcdn.com/tos-useast2a-avt-0068-giso/accfb0bfc0681ffeb28ed21977a50089~c5_100x100.jpg?x-expires=1675904400&amp;x-signature=EuRWwbg%2Bw1oCbudeJ6tnviiI%2FRA%3D" class="tiktok-1zpj2q-ImgAvatar e1e9er4e1">
      </span>
    </a>
    <div class="tiktok-1mf23fd-DivContentContainer e1g2efjf1">
      <a class="tiktok-bhsg9d-StyledUserLinkName e1g2efjf4" href="/@mrsyanjun2408">
        <span data-e2e="comment-username-1" class="tiktok-mfqbp1-SpanUserNameText e1g2efjf3">Jkjkjk </span>
      </a>
      <p data-e2e="comment-level-1" class="tiktok-q9aj5z-PCommentText e1g2efjf6">
        <span>Dlu suka pakai bawal mcm ni zmn2 reformasi😂.dia pakaila senget mcm mana pn cantik jee</span>
      </p>
      <p class="tiktok-1wmf4bu-PCommentSubContent e1g2efjf8">
        <span data-e2e="comment-time-1">2022-4-19</span>
        <span data-e2e="comment-reply-1" class="tiktok-nqnosi-SpanReplyButton e1g2efjf9">Reply</span>
      </p>
    </div>
    <div class="tiktok-mnluvt-DivActionContainer esns4rh0">
      <div class="tiktok-5g6iif-DivMoreContainer esns4rh1">
        <div data-e2e="comment-more-icon">
          <svg class="tiktok-fzlfzu-StyledMoreIcon esns4rh2" width="1em" data-e2e="" height="1em" viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M4 24C4 21.7909 5.79086 20 8 20C10.2091 20 12 21.7909 12 24C12 26.2091 10.2091 28 8 28C5.79086 28 4 26.2091 4 24ZM20 24C20 21.7909 21.7909 20 24 20C26.2091 20 28 21.7909 28 24C28 26.2091 26.2091 28 24 28C21.7909 28 20 26.2091 20 24ZM36 24C36 21.7909 37.7909 20 40 20C42.2091 20 44 21.7909 44 24C44 26.2091 42.2091 28 40 28C37.7909 28 36 26.2091 36 24Z"></path>
          </svg>
        </div>
      </div>
      <div class="tiktok-1wyxwrs-DivLikeWrapper ezxoskx0">
        <div data-e2e="comment-like-icon">
          <svg width="20" data-e2e="" height="20" viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M24 9.01703C19.0025 3.74266 11.4674 3.736 6.67302 8.56049C1.77566 13.4886 1.77566 21.4735 6.67302 26.4016L22.5814 42.4098C22.9568 42.7876 23.4674 43 24 43C24.5326 43 25.0432 42.7876 25.4186 42.4098L41.327 26.4016C46.2243 21.4735 46.2243 13.4886 41.327 8.56049C36.5326 3.736 28.9975 3.74266 24 9.01703ZM21.4938 12.2118C17.9849 8.07195 12.7825 8.08727 9.51028 11.3801C6.16324 14.7481 6.16324 20.214 9.51028 23.582L24 38.1627L38.4897 23.582C41.8368 20.214 41.8368 14.7481 38.4897 11.3801C35.2175 8.08727 30.0151 8.07195 26.5062 12.2118L26.455 12.2722L25.4186 13.3151C25.0432 13.6929 24.5326 13.9053 24 13.9053C23.4674 13.9053 22.9568 13.6929 22.5814 13.3151L21.545 12.2722L21.4938 12.2118Z"></path>
          </svg>
        </div>
        <span data-e2e="comment-like-count" class="tiktok-1k32hld-SpanCount ezxoskx2" style="margin-left: 0px; margin-right: 0px;">234</span>
      </div>
    </div>
  </div>
  <div class="tiktok-zn6r1p-DivReplyContainer eo72wou1">
    <div class="tiktok-1for4nf-DivReplyActionContainer eo72wou2">
      <p data-e2e="view-more-1" class="tiktok-1qqecn-PReplyActionText eo72wou4">View more replies (3) <svg class="tiktok-1w2nwdz-StyledChevronDownFill eo72wou3" width="1em" data-e2e="" height="1em" viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M21.8788 33.1213L7.58586 18.8284C7.19534 18.4379 7.19534 17.8047 7.58586 17.4142L10.4143 14.5858C10.8048 14.1953 11.438 14.1953 11.8285 14.5858L24.0001 26.7574L36.1716 14.5858C36.5622 14.1953 37.1953 14.1953 37.5859 14.5858L40.4143 17.4142C40.8048 17.8047 40.8048 18.4379 40.4143 18.8284L26.1214 33.1213C24.9498 34.2929 23.0503 34.2929 21.8788 33.1213Z"></path>
        </svg>
      </p>
    </div>
  </div>
</div>
    """
    return lol


def tiktok_comments_html(avatar, username, nickname, comment, posted_date, likes, noOfRepliedComments):
    lol ="""
<div class="tiktok-16r0vzi-DivCommentItemContainer eo72wou0">
  <div id="7088335299323446017" class="tiktok-1kimton-DivCommentContentContainer e1g2efjf0">
    <a data-e2e="comment-avatar-1" class="tiktok-cwmrys-StyledUserLinkAvatar e1g2efjf5" href="/@mrsyanjun2408" style="flex: 0 0 40px;">
      <span shape="circle" data-e2e="" class="tiktok-tuohvl-SpanAvatarContainer e1e9er4e0" style="width: 40px; height: 40px;">
        <img loading="lazy" src="{}">
      </span>
    </a>
    <div class="tiktok-1mf23fd-DivContentContainer e1g2efjf1">
      <a class="tiktok-bhsg9d-StyledUserLinkName e1g2efjf4" href="https://www.tiktok.com/{}">
        <span data-e2e="comment-username-1" class="tiktok-mfqbp1-SpanUserNameText e1g2efjf3">{}</span>
      </a>
      <p data-e2e="comment-level-1" class="tiktok-q9aj5z-PCommentText e1g2efjf6">
        <span>{}</span>
      </p>
      <p class="tiktok-1wmf4bu-PCommentSubContent e1g2efjf8">
        <span data-e2e="comment-time-1">{}</span>
        <span data-e2e="comment-reply-1" class="tiktok-nqnosi-SpanReplyButton e1g2efjf9">Reply</span>
      </p>
    </div>
    <div class="tiktok-mnluvt-DivActionContainer esns4rh0">
      <div class="tiktok-5g6iif-DivMoreContainer esns4rh1">
        <div data-e2e="comment-more-icon">
          <svg class="tiktok-fzlfzu-StyledMoreIcon esns4rh2" width="1em" data-e2e="" height="1em" viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M4 24C4 21.7909 5.79086 20 8 20C10.2091 20 12 21.7909 12 24C12 26.2091 10.2091 28 8 28C5.79086 28 4 26.2091 4 24ZM20 24C20 21.7909 21.7909 20 24 20C26.2091 20 28 21.7909 28 24C28 26.2091 26.2091 28 24 28C21.7909 28 20 26.2091 20 24ZM36 24C36 21.7909 37.7909 20 40 20C42.2091 20 44 21.7909 44 24C44 26.2091 42.2091 28 40 28C37.7909 28 36 26.2091 36 24Z"></path>
          </svg>
        </div>
      </div>
      <div class="tiktok-1wyxwrs-DivLikeWrapper ezxoskx0">
        <div data-e2e="comment-like-icon">
          <svg width="20" data-e2e="" height="20" viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M24 9.01703C19.0025 3.74266 11.4674 3.736 6.67302 8.56049C1.77566 13.4886 1.77566 21.4735 6.67302 26.4016L22.5814 42.4098C22.9568 42.7876 23.4674 43 24 43C24.5326 43 25.0432 42.7876 25.4186 42.4098L41.327 26.4016C46.2243 21.4735 46.2243 13.4886 41.327 8.56049C36.5326 3.736 28.9975 3.74266 24 9.01703ZM21.4938 12.2118C17.9849 8.07195 12.7825 8.08727 9.51028 11.3801C6.16324 14.7481 6.16324 20.214 9.51028 23.582L24 38.1627L38.4897 23.582C41.8368 20.214 41.8368 14.7481 38.4897 11.3801C35.2175 8.08727 30.0151 8.07195 26.5062 12.2118L26.455 12.2722L25.4186 13.3151C25.0432 13.6929 24.5326 13.9053 24 13.9053C23.4674 13.9053 22.9568 13.6929 22.5814 13.3151L21.545 12.2722L21.4938 12.2118Z"></path>
          </svg>
        </div>
        <span data-e2e="comment-like-count" class="tiktok-1k32hld-SpanCount ezxoskx2" style="margin-left: 0px; margin-right: 0px;">{}</span>
      </div>
    </div>
  </div>
  <div class="tiktok-zn6r1p-DivReplyContainer eo72wou1">
    <div class="tiktok-1for4nf-DivReplyActionContainer eo72wou2">
      <p data-e2e="view-more-1" class="tiktok-1qqecn-PReplyActionText eo72wou4">View more replies ({}) <svg class="tiktok-1w2nwdz-StyledChevronDownFill eo72wou3" width="1em" data-e2e="" height="1em" viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M21.8788 33.1213L7.58586 18.8284C7.19534 18.4379 7.19534 17.8047 7.58586 17.4142L10.4143 14.5858C10.8048 14.1953 11.438 14.1953 11.8285 14.5858L24.0001 26.7574L36.1716 14.5858C36.5622 14.1953 37.1953 14.1953 37.5859 14.5858L40.4143 17.4142C40.8048 17.8047 40.8048 18.4379 40.4143 18.8284L26.1214 33.1213C24.9498 34.2929 23.0503 34.2929 21.8788 33.1213Z"></path>
        </svg>
      </p>
    </div>
  </div>
</div>
    """.format(avatar, username , nickname, comment, posted_date, likes, noOfRepliedComments)
    return lol



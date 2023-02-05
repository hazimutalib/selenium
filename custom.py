import streamlit as st

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
    width: 1200px;
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
    margin-right: 3.0em;
    margin-bottom: 1em;
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
    </style>
    """, unsafe_allow_html=True)


def tiktok_video_css():
    st.sidebar.markdown(""" 
    <style>
    .tiktok-u7bnsh-DivItemContainer {
        margin-right: 14px;
        margin-left: 25%;
        width: 147px;
        margin-bottom: 16px;
        cursor: pointer;
    }
    .tiktok-1ys5eyp-DivCoverContainer {
        width: 100%;
        height: 202px;
        position: relative;
        border-radius: 8px;
        margin-bottom: 8px;
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
    st.markdown("""<div id="container">
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
    """.format(total_videos, total_comments, total_user), unsafe_allow_html=True)


def tiktok_video(tiktok_link, tiktok_image, tiktok_caption, tiktok_creator, posted_date, tiktok_views, tiktok_likes):
    st.sidebar.markdown(""" 
    <div class="tiktok-u7bnsh-DivItemContainer e1ymawm01">
      <div class="tiktok-1ys5eyp-DivCoverContainer e1ymawm02">
        <a href = "{}"> 
        <img src="{}" class="tiktok-m86b9p-ImgCover e1ymawm04">
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
    """.format(tiktok_link, tiktok_image, tiktok_caption, tiktok_creator, posted_date, tiktok_views, tiktok_likes), unsafe_allow_html=True,)
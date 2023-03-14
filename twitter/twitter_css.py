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

def tweets_css(img2):

    if len(str(img2)) == 0:
      st.markdown("""
      <style>
      img {
      max-width:100%;
      display: inline-block;
    }
      p {
      font-size: 0.9rem;
    }
    .avator {
      border-radius:100px;
      width:48px;
      margin-right: 15px;
    }


    .tweet-wrap {
      max-width:490px;
      background: #fff;
      margin: 0 auto;
      margin-top: 50px;
      border-radius:3px;
      padding: 30px;

    }

    .tweet-header {
      display: flex;
      align-items:flex-start;
      font-size:14px;
    }
    .tweet-header-info {
      font-weight:bold;
    }
    .tweet-header-info span {
      color:#657786;
      font-weight:normal;
      margin-left: 5px;
    }
    .tweet-header-info p {
      font-weight:normal;
      margin-top: 5px;
      
    }
    .tweet-img-wrap {
      padding-left: 60px;
    }

    .tweet-info-counts {
      display: flex;
      margin-left: 60px;
      margin-top: 10px;
    }
    .tweet-info-counts div {
      display: flex;
      margin-right: 20px;
    }
    .tweet-info-counts div svg {
      color:#657786;
      margin-right: 10px;
    }
    @media screen and (max-width:430px){
      body {
        padding-left: 20px;
        padding-right: 20px;
      }
      .tweet-header {
        flex-direction:column;
      }
      .tweet-header img {
        margin-bottom: 20px;
      }
      .tweet-header-info p {
        margin-bottom: 30px;
      }
      .tweet-img-wrap {
        padding-left: 0;
      }
      .tweet-info-counts {
      display: flex;
      margin-left: 0;
    }
    .tweet-info-counts div {
      margin-right: 10px;
    }


      </style>
      """, unsafe_allow_html=True,)
    else:
      st.markdown("""
      <style>
      img {
      max-width:45%;
      display: inline-block;
    }
    .avator {
      border-radius:100px;
      width:48px;
      margin-right: 15px;
    }


    .tweet-wrap {
      max-width:490px;
      background: #fff;
      margin: 0 auto;
      margin-top: 50px;
      border-radius:3px;
      padding: 30px;
    }

    .tweet-header {
      display: flex;
      align-items:flex-start;
      font-size:14px;
    }
    .tweet-header-info {
      font-weight:bold;
      
    }
    .tweet-header-info span {
      color:#657786;
      font-weight:normal;

      margin-left: 5px;
    }
    .tweet-header-info p {
      font-weight:normal;
      margin-top: 5px;
      
    }
    .tweet-img-wrap {
      padding-left: 60px;
    }

    .tweet-info-counts {
      display: flex;
      margin-left: 60px;
      margin-top: 10px;
    }
    .tweet-info-counts div {
      display: flex;
      margin-right: 20px;
    }
    .tweet-info-counts div svg {
      color:#657786;
      margin-right: 10px;
    }
    @media screen and (max-width:430px){
      body {
        padding-left: 20px;
        padding-right: 20px;
      }
      .tweet-header {
        flex-direction:column;
      }
      .tweet-header img {
        margin-bottom: 20px;
      }
      .tweet-header-info p {
        margin-bottom: 30px;
      }
      .tweet-img-wrap {
        padding-left: 0;
      }
      .tweet-info-counts {
      display: flex;
      margin-left: 0;
    }
    .tweet-info-counts div {
      margin-right: 10px;
    }


      </style>
      """, unsafe_allow_html=True,)
      
        






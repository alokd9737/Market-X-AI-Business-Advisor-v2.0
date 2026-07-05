def load_css():

    return """

<style>

.stApp{

background:#F7F8FA;

font-family:Inter,sans-serif;

}

.block-container{

padding-top:1rem;

padding-left:3rem;

padding-right:3rem;

padding-bottom:2rem;

}

section[data-testid="stSidebar"]{

background:#081C3A;

}

section[data-testid="stSidebar"] *{

color:white;

}

.hero{

background:white;

padding:45px;

border-radius:18px;

box-shadow:0px 10px 30px rgba(0,0,0,.08);

margin-bottom:30px;

}

.hero-title{

font-size:46px;

font-weight:800;

color:#081C3A;

}

.hero-sub{

font-size:20px;

color:#4B5563;

margin-top:10px;

}

.card{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0px 8px 20px rgba(0,0,0,.05);

border:1px solid #E5E7EB;

margin-bottom:20px;

}

.metric-card{

background:white;

padding:22px;

border-radius:16px;

border-left:6px solid #C9A227;

box-shadow:0px 6px 18px rgba(0,0,0,.06);

}

.footer{

margin-top:40px;

text-align:center;

color:#6B7280;

font-size:14px;

}

.stButton>button{

background:#0B1F3A;

color:white;

border-radius:12px;

height:52px;

font-size:17px;

font-weight:600;

border:none;

}

.stButton>button:hover{

background:#123D73;

}

.stTextInput>div>div>input{

border-radius:12px;

}

.stTextArea textarea{

border-radius:12px;

}

div[data-testid="stMetric"]{

background:white;

padding:18px;

border-radius:16px;

border:1px solid #E5E7EB;

}
.card:hover{

transform:translateY(-5px);

transition:.25s;

box-shadow:0px 18px 35px rgba(0,0,0,.12);

}

</style>

"""

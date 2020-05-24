from pesummary.core.webpage.webpage import make_html, open_html

make_html(
    web_dir="../", pages=["home"], stylesheets=[], title="Charlie Hoy"
)
index = open_html("../", "../", "home")
index.add_content(
"""
    <script src='./js/navigation.js'></script>
    <link rel="stylesheet" href="./css/fa-code.css">
    <link rel="stylesheet" href="./css/parallax.css">
    <link rel="stylesheet" href="./css/text.css">

<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<div class="parallax1"></div>
<h1 id="name">Charlie<br>Hoy<br></h1>
<h1 id="occupation">PhD student</h1>
<div class="container" style="position: absolute; left: 11%; top:410px">
<a href='https://www.google.co.uk' class="fa fa-facebook-square" style="font-size: 30px; padding-right: 3px"></a>
<a href='http://linkedin.com/in/charlie-hoy-46405a161' class="fa fa-linkedin-square" style="font-size: 30px; padding-right: 3px"></a>
<a href='https://github.com/hoyc1' class="fa fa-github-square" style="font-size: 30px; padding-right: 3px"></a>
<a href='https://git.ligo.org/charlie.hoy' class="fa fa-gitlab" style="font-size: 30px; padding-right: 3px"></a>
<a href="mailto:hoyc1@cardiff.ac.uk" class="fa fa-envelope" style="font-size: 30px; padding-right: 3px"></a>
</div>

<div class="container" style="position: absolute; left: 50%; margin-left: -150px; top:475px; border-style: solid; border-width: thick; border-color: #f8f8ff; height: 450px; width: 300px">
    <img src="./images/charliehoy.jpg" style="width: 250px; position: absolute; margin-top: 10px" href="https://scholar.google.com/citations?view_op=list_works&hl=en&authuser=1&user=wjjomcQAAAAJ&gmla=AJsN-F6xnalxEPJ-nK_7H_R0RRFxJA9kpJ6af7mKkULPtRTS0ch-kAu4xF_GgLdeu_Dg95EQwJOk3mUC1qS2aVas2waVCwiIe-D1i6cwM8QZjKXServlZzA"></img>
    <div class="row justify-content-center">
    <a href='https://scholar.google.com/citations?view_op=list_works&hl=en&authuser=1&user=wjjomcQAAAAJ&gmla=AJsN-F6xnalxEPJ-nK_7H_R0RRFxJA9kpJ6af7mKkULPtRTS0ch-kAu4xF_GgLdeu_Dg95EQwJOk3mUC1qS2aVas2waVCwiIe-D1i6cwM8QZjKXServlZzA' data-toggle='tooltip'>
    <h1 style="margin-top: 350px; font-size: 24px; color: #f8f8ff">Google Scholar page</h1>
    </a>
    </div>
</div>

<div class="parallax2"></div>
<div class="container" style="position: absolute; left: 10%; top: 1000px; padding-bottom: 10%">
<div class="container" style="border-style: solid; border-width: thick; border-color: #f8f8ff; padding-bottom: 2%">
<div class="card job" style="margin-top: 20px">
    <div class="card-header bg-dark text-white">
        PhD student, <span class="institution">Cardiff University</span> (2018-Present)
    </div>
    <div class="card-body">
      <i>Proposed thesis title: Binary Black Hole Astrophysics</i>,

<ul class="pt-2">
<li>Understanding when precession can be measured from a compact binary coalesence</li>
<li>Inferring the preferred spin distribution of Black Holes</li>
<li>development of software and documentation to support study of open data by the wider scientific community and the public</li>
</ul>

Funded by STFC
    </div>
  </div>
</div>
<div class="container" style="border-style: solid; border-width: thick; border-color: #f8f8ff; padding-bottom: 2%">
<div class="card job" style="margin-top: 20px">
    <div class="card-header bg-dark text-white">
        Other interests
    </div>
    <div class="card-body">
<ul class="pt-2">
<li>Software development</li>
<li>Numerically solving Einstein's equations</li>
<li>Modelling binary black populations</li>
</ul>
    </div>
  </div>
</div>
</div>

<div class="container" style="padding-bottom: 5%">
<h1 id="publication">Publications</h1>
<h1 style="margin-top: 150px" id="publicationtext">The list below includes all publications on which I had a significant contribution to the work presented. Not included are a number of publications on which I am named as an author by virtue of being a member of the LIGO Scientific Collaboration.</h1>
<div style="margin-top: 50px">
<script src="https://bibbase.org/show?bib=https%3A%2F%2Fraw.githubusercontent.com%2Fhoyc1%2Fhoyc1.github.io%2Fmaster%2Fsrc%2Fbibtex.bib&jsonp=1"></script>
</div>
</div>
<div class="bg-dark text-light" style="background-color: lightgrey; padding-bottom: 5%">
<div class="container">
<h1 id="awards">Awards</h1>
<table class="table" style="width:100%; background-color: #f8f8ff; border-color: #f8f8ff margin-bottom: 100px">
  <tr>
    <td><a href="https://cqgplus.com/2019/05/13/charlie-hoy-and-lasse-schmieding-win-best-student-talk-prizes-at-britgrav-2019/">Best student talk prizes at Britgrav 2019, Durham</a></td>
  </tr>
  <tr>
    <td>Best poster at the Early Career Researcher poster competition 2019, Cardiff</td>
  </tr>
  <tr>
    <td>$1500 AUSD grant to support travel to Melbourne, Australia for the Parameter Estimation workshop, 2019</td>
  </tr>
</table>
  </div>
</div>
</div>
</div>

<style>
/* Responsive columns */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
}
</style>

<div class="bg-warning text-light" style="background-color: yellow; margin-top: 10px; padding-bottom: 5%">
<div class="container">
<h1 id="git_projects">Git projects</h1>
<div class="card-columns">
   <div class="column">
      <div class="card mb-4 bg-dark text-light">
        <div class="card-body">
          <h3 class="card-title">PESummary</h3>
          <p class="card-text">A collaboration-driven Python package providing tools for generating summary pages for all sample generating codes.<br><img src="https://badge.fury.io/py/pesummary.svg"></img><img src="https://img.shields.io/conda/vn/conda-forge/pesummary.svg" style="margin-left: 5px"></img><br><img src="https://img.shields.io/pypi/dm/pesummary"></img><img src="https://anaconda.org/conda-forge/pesummary/badges/downloads.svg" style="margin-left: 5px"></img>
        </p></div>
        <div class="card-footer">
          <a href="https://git.ligo.org/lscsoft/pesummary" target="_blank"><i class="fa fa-gitlab" style="padding-right: 5px;"></i>lscsoft/pesummary</a>
        </div>
      </div>
      <div class="card mb-4 bg-dark text-light">
        <div class="card-body">
          <h3 class="card-title">This website</h3>
          <p class="card-text">Source code for this website written in HTML, CSS and Javascript
        </p></div>
        <div class="card-footer">
          <a href="https://github.com/hoyc1/hoyc1.github.io" target="_blank"><i class="fa fa-github" style="padding-right: 5px;"></i>hoyc1/hoyc1.github.io</a>
        </div>
      </div>
   </div>
</div>
</div>
</div>
<div class="bg-dark text-light" style="margin-bottom: 10px; height: 70px">
  <div class="row justify-content-center" style="margin-top: 10px">
    <h1 style="font-size: 30px">© Charlie Hoy</h1>
  </div>
</div>
"""
)

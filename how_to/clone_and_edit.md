<!-- Add banner here -->

[![Header](https://github.com/caly-pso/covid_app/blob/main/img/header.png)](#TL;DR)


# How to Clone and Edit This Repo



## TL;DR

How I created my portfolio website using Bootstrap, hosted for free on GitHub Pages.

<br>


# Table of contents

- [How to Clone and Edit This Repo](#repo)
- [TL;DR](#TL;DR)
- [Table of contents](#table-of-contents)
- [Cloning the Repo](#clone)
- [Making Changes](#edit)
- [Use GitHub Pages to Host](#hosting)

<br>

# How to Clone and Edit This Repo

###### [(Back to top)](#table-of-contents)

<details><summary>Using Git</summary>
<br>
<p>
    Navigate to the folder you wish to use:
    
    cd Users/me/Desktop
</p>
<p>
    Initalize git:
    
    git init
</p>
<p>
    Clone the repo:

    git clone https://github.com/caly-pso/portfolio_website_template.git
</p>
</details>

OR

<details>
<summary>Downloading the Zip file</summary>
<br>
    <ul>
    <li>Open the <a class="nav-link" href="https://github.com/caly-pso/portfolio_website_template" target="_blank">repo</a> in your browser</li>
    <li>Click the green download code button towards the top right</li>
    <li>Download the repo as a zip</li>
    <li>Unzip the files and place them in the folder you wish to work with</li>
    </ul>
</details>

<br>


# Making Changes

###### [(Back to top)](#table-of-contents)

<p align="center">
  <img width="300" src="https://github.com/caly-pso/caly-pso.github.io/blob/main/how_to/img/file_structure.png">
</p>

Now that you have the files on your local computer, you can open them in a text editor. The file structure should be what you see above. 

The first thing you will want to do is to customize the index.html page. This includes a projects section, about section, resume section, and a footer where you can link your GitHub, Twitter, etc. 

##### Step 1: Put in your name 
At the top, in the about section, and anywhere else you want to display it.

##### Step 2: Update the sections 
Customize the projects section with images of your own projects and place them in the assets/img/portfolio folder. Update the path names of the images displayed, and link them to your GitHub to display the code.

Add your image to the About section, as well as your city, email, interests, and skills.

Put in your resume. Type out your schooling and experience directly into the HTML, and link a PDF version of your resume to the Download Here button. Currently the PDF example is saved in the assets/img folder, where you can save your own.

Add links to your GitHub, LinkedIn, Medium, Twitter, Youtube, etc. You can find the associated icons on [Font Awesome](https://fontawesome.com/icons?d=gallery), and add in the link to the i tag class. 

#### Step 3: Update the Isotope filter
In order to sort and filter the projects, I used the plugin Isotope. You can customize these filters to be anything you want. But make sure you change both the filter options under the `ul id="portfolio-fltrs"` secttion, and within each portfolio item's div class.

<br>


# Use GitHub Pages to Host

###### [(Back to top)](#table-of-contents)

[GitHub Pages](https://pages.github.com/)

#### Now that you have made the website your own, you can host it for free on GitHub. The simplest way is to:

1. Make sure you have a GitHub account
2. Create a new reposittory with the following selections
    - Repo Name: username.github.io (for example I named mine: caly-pso.github.io). This is what will show up in the URL
    - Check "Initialize Repository with a README"
    - Select "Create repository"
3. Now that the repo is made, in GitHub, select the dropdown "Add file" and choose "Upload files". Now drag and drop the files in your portfolio folder into the browser. Once uploaded, commit your changes.

OR

<details>
<summary><strong>Using Git</strong></summary>
<br>
    <ol>
        <li>Make sure you have a GitHub account</li>
        <li>Create a new repository with the following selections
            <ul><li>Repo Name: username.github.io (for example I named mine: caly-pso.github.io). This is what will show up in the URL</li>
                <li>Check "Initialize Repository with a README"</li>
                <li>Select "Create repository"</li>
            </ul>
        </li>
        <li>Clone the repository you just created: 
                
git clone https://github.com/username/username.github.io
                
</li>
            <li>Open the project's folder: 
                
cd username.github.io

</li>
            <li>Add, commit, and push your changes: 
                git add --all

git commit -m "Initial commit"

git push -u origin main 
        
</li></ol>
        
</details>

#### Finally:
Ater 5-10 minutes your website will be viewable at: https://username.github.io. If it is not there, check your repo's setting to ensure the GitHub Pages source is pointing to the correct branch. 

<br>

# About:

I created this website to improve my own skills and am happy to share it! To see my other projects check out my [GitHub](https://github.com/caly-pso). 

<!-- To learn how to make your own website, similar to mine, [check out how it was made](https://github.com/caly-pso/caly-pso.github.io/blob/main/how_to/create_a_bootstrap_website.md)! -->

###### [(Back to top)](#table-of-contents)

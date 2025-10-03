---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 👋 About Me

I am currently pursuing my PhD in the Department of Geographical Sciences at the University of Maryland, College Park.  
My research explores remote sensing and knowledge-guided machine learning for understanding climate and ecosystems.  
I have authored over 11 papers in top journals and international AI conferences with a total of 
<a href='https://scholar.google.com/citations?user=f0840jkAAAAJ&hl=en'>Google Scholar citations <strong><span id='total_cit'></span></strong></a>.

📧 Email: [shuoxu98@terpmail.umd.edu](mailto:shuoxu98@terpmail.umd.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/shuoxuphd/) | [Google Scholar](https://scholar.google.com/citations?user=f0840jkAAAAJ&hl=en)

---

# 🔥 News
- *2025.09*: &nbsp;🎉🎉 One paper accepted by NeurIPS 2025! 


# 📖 Educations
- *2021.09 – Present* Ph.D. candidate, Geographic Information Science and Cartography, **University of Maryland**, College Park, MD, USA
- *2018.09 – 2021.06* M.S., Cartography and Geography Information System, **Beijing Normal University**, Beijing, China
- *2014.09 – 2018.06* B.S., Remote Sensing Science and Technology, **Shandong University of Science and Technology**, Qingdao, China

---

# 🔬 Research Interests
- Remote Sensing and Multi-Source Data Fusion for Climate Solutions  
- Machine Learning and Quantitative Analysis for Earth and Ecosystem Systems  
- Time Series and Spatial Analysis to Identify High-Leverage Pathways for Climate Mitigation  

---

# 🛠 Technical Skills
- **Programming & Analysis:** Python, MATLAB, IDL; HPC for Large-Scale Datasets  
- **Geospatial Tools:** Google Earth Engine, ArcPro, ENVI, ERDAS  
- **Machine Learning & Frameworks:** PyTorch, TensorFlow; Data-Driven & Physics-Guided ML  
- **Specialties:** Spatial and Temporal Data Analysis, Climate & Ecosystem Modeling  

---

# 💼 Work Experience

### Research Assistant — University of Maryland  
*Sep 2021 – Present*  
**NSF-Funded Project: Improving the Ecosystem Demography (ED) Model with AI**  
- Developed transformer-based ML frameworks integrating satellite, model, and in-situ data.  
- Generated time series of carbon stocks, fluxes, and vegetation dynamics.  
- Applied spatial and temporal analyses to inform climate mitigation and policy.

**NOAA-Funded Project: Enhancing NOAA VIIRS Land Surface Temperature Product**  
- Designed multi-source fusion algorithms for all-weather VIIRS LST product.  
- Built data pipelines (Python/TensorFlow, MATLAB) to produce global LST time series and anomalies.  
- Presented findings at AGU, AMS, and NOAA, recognized for applied climate solutions.

---

# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A novel approach to estimate land surface temperature from Landsat top-of-atmosphere reflective and emissive data using transfer-learning neural network](https://doi.org/10.1016/j.scitotenv.2024.176783)  

**Shuo Xu**, Wang, D., Liang, S., Jia, A., Li, R., Wang, Z., & Liu, Y.

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=f0840jkAAAAJ&citation_for_view=f0840jkAAAAJ:ALROH1vI_8AC)
<strong><span class='show_paper_citations' data='f0840jkAAAAJ:ALROH1vI_8AC'></span></strong>

- Publicly released the algorithm on Google Earth Engine to support broader applications.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">IEEE GRSM 2024</div>
      <img src='images/lst_review.png' alt="LST Review" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Advances in Methodology and Generation of All-Weather Land Surface Temperature Products From Polar-Orbiting and Geostationary Satellites: A Comprehensive Review](https://doi.org/10.1109/MGRS.2024.3325375)  

Jia, A., Liang, S., Wang, D., Mallick, K., Zhou, S., Hu, T., **Shuo Xu**, et al.

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=f0840jkAAAAJ&citation_for_view=f0840jkAAAAJ:IWHjjKOFINEC)
<strong><span class='show_paper_citations' data='f0840jkAAAAJ:IWHjjKOFINEC'></span></strong>

- Comprehensive review of methods for generating all-weather land surface temperature products integrating multiple satellite data sources.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge">RSE 2021</div>
      <img src='images/cdf_mkf.png' alt="CDF MKF" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[A new land surface temperature fusion strategy based on cumulative distribution function matching and multiresolution Kalman filtering](https://doi.org/10.1016/j.rse.2020.112256)  

**Shuo Xu**, Cheng, J.

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=f0840jkAAAAJ&citation_for_view=f0840jkAAAAJ:u-x6o8ySG0sC)
<strong><span class='show_paper_citations' data='f0840jkAAAAJ:u-x6o8ySG0sC'></span></strong>

- Ranked among the top 1% most-cited Environment/Ecology articles published in 2021; method adopted to generate widely used temperature datasets.
</div>
</div>

<div style="clear: both;"></div>

- [Assessment of gridded datasets of various near surface temperature variables over Heihe River Basin: Uncertainties, spatial heterogeneity and clear-sky bias](https://doi.org/10.1016/j.jag.2023.103347). *International Journal of Applied Earth Observation and Geoinformation, 2023.*  
- [Assessing the reliability of the MODIS LST product to detect temporal variability](https://doi.org/10.1109/LGRS.2023.3268803). *IEEE GRSL, 2023.*  
- [A random forest-based data fusion method for obtaining all-weather land surface temperature with high spatial resolution](https://doi.org/10.3390/rs13112211). *Remote Sensing, 2021.*  
- [Reconstructing all-weather land surface temperature using the Bayesian maximum entropy method over the Tibetan Plateau and Heihe River Basin](https://doi.org/10.1109/JSTARS.2019.2927726). *IEEE JSTARS, 2019.*  

---

# 🎖 Honors and Awards

- *2025* &nbsp;🏆 Ann G. Wylie Dissertation Fellowship, University of Maryland
- *2025* &nbsp;🏆 Excellence in Graduate Research Award (Second Place), University of Maryland
- *2025* &nbsp;🏆 GIS Summer Research Fellowship, University of Maryland
- *2024* &nbsp;🏆 Outstanding Graduate Research Assistant Award, University of Maryland
- *2024* &nbsp;🏆 Excellence in Graduate Research Award (Third Place), University of Maryland
- *2024* &nbsp;🏆 Jingli Yang Summer Research Fellowship, University of Maryland
- *2024* &nbsp;🏆 Graduate Travel Fellowship, University of Maryland
- *2022* &nbsp;🏆 Jacob K. Goldhaber Travel Grant, University of Maryland
- *2021* &nbsp;🏆 Outstanding Graduate, Beijing Normal University
- *2021* &nbsp;🏆 Zhou Tingru Scholarship, Beijing Normal University
- *2020* &nbsp;🏆 National Scholarship, Beijing Normal University
- *2019* &nbsp;🏆 First-class Scholarship, Beijing Normal University

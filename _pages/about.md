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

Hi, I am a **Ph.D. candidate**, advised by Dr. Yiqun Xie, in the Department of Geographical Sciences at the **University of Maryland**, College Park. 
My primary research focus on **remote sensing and knowledge-guided machine learning**, with expertise in satellite data retrieval, data downscaling and multi-source data fusion, all-weather product development, and addressing related scientific challenges.   
I have **authored over 11 papers** in top journals and international AI conferences with a total of 
<a href='https://scholar.google.com/citations?user=f0840jkAAAAJ&hl=en'>Google Scholar citations <strong><span id='total_cit'></span></strong></a>. I also serve as a **reviewer for 14 international journals**, including *Remote Sensing of Environment (RSE)* (Impact Factor = 11.4).

---

<span class='anchor' id='news'></span>
# 🔥 News
- *2025.09*: &nbsp;🎉🎉 Paper accepted by **NeurIPS 2025**!
- *2025.01*: &nbsp;🎉🎉 RSE paper ranked among the **top 1% most cited** (Environment/Ecology 2021) and the dataset has been accessed **46,000+** times worldwide.
- *2024.12*: &nbsp;🎉🎉 Paper published in **IEEE MGRS (Impact Factor = 16.4)**!
- *2024.12*: &nbsp;🎉🎉 Paper published in **STOTEN (Impact Factor = 8.0)**!
- *2024.03*: &nbsp;🎉🎉 Paper published at **AAAI 2024**!

---

# 🔬 Research Interests
- Remote Sensing and Multi-Source Data Fusion  
- Knowledge-guided Machine Learning and Quantitative Analysis  
- Time Series Modeling and Forecasting  

---

# 🛠 Technical Skills
- **Programming & Analysis:** Python, MATLAB, IDL; High Performance Computing for Large-Scale Datasets  
- **Geospatial Tools:** Google Earth Engine, ArcPro, ENVI, ERDAS  
- **Machine Learning & Frameworks:** PyTorch, TensorFlow; Data-Driven and Knowledge-Guided Machine Learning  
- **Specialties:** Temporal Prediction, Spatiotemporal Data Analysis, and Ecosystem Modeling  

---

<span class='anchor' id='publications'></span>
# 📝 Peer-review Publications

<span style="background-color:#2E8B57;color:white;padding:2px 6px;border-radius:4px;">AI Conference Paper</span> 
<span style="background-color:#1E90FF;color:white;padding:2px 6px;border-radius:4px;">Journal Paper</span>
&nbsp;&nbsp;

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-conference">NeurIPS 2025</div>
      <!-- <img src='images/Carbon.png' alt="Carbon Bench" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

Carbon-Bench: A forty-year global-scale benchmark dataset for carbon forecasting in forest ecosystems  

Zhihao Wang, Yiqun Xie, Lei Ma, George Hurtt, Xiaowei Jia, Yanhua Li, Ruohan Li, Zhili Li, **Shuo Xu**.
<br><em>NeurIPS 2025 (Datasets and Benchmarks Track), San Diego, CA, 2025</em>.

</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-conference">AAAI 2024</div>
      <!-- <img src='images/SimFair.png' alt="SimFair" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[SimFair: Physics-guided fairness-aware learning with simulation models](https://arxiv.org/abs/2401.15270)  

Zhihao Wang, Yiqun Xie, Zhili Li, Xiaowei Jia, Zhe Jiang, Aolin Jia, **Shuo Xu**.
<br><em>The 38th AAAI Conference on Artificial Intelligence (AAAI'24), Vancouver, Canada, 2024</em>.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">RSE 2021</div>
      <!-- <img src='images/cdf.jpg' alt="CDF MKF" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[A new land surface temperature fusion strategy based on cumulative distribution function matching and multiresolution Kalman filtering](https://doi.org/10.1016/j.rse.2020.112256)  

  **Shuo Xu**, Jie Cheng.
  <br><em>Remote Sensing of Environment, 2021, Impact Factor = 11.4</em>.

  - Ranked among the top 1% most-cited Environment/Ecology articles published in 2021.
  - Method adopted to generate a widely used temperature dataset, accessed 46,000+ times worldwide.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">STOTEN 2024</div>
      <!-- <img src='images/trans.jpg' alt="sym" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

  [A novel approach to estimate land surface temperature from Landsat top-of-atmosphere reflective and emissive data using transfer-learning neural network](https://doi.org/10.1016/j.scitotenv.2024.176783)  

  **Shuo Xu**, Dongdong Wang, Shunlin Liang, Aolin Jia, Ruohan Li, Zhihao Wang, Yuling Liu.
  <br><em>Science of The Total Environment, 2024, Impact Factor = 8.0</em>.
  - Publicly released the algorithm on Google Earth Engine to support broader applications.

</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">Int. J. Appl. Earth Obs. Geoinf 2023</div>
      <!-- <img src='images/vali.png' alt="CDF MKF" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Assessment of gridded datasets of various near surface temperature variables over Heihe River Basin: Uncertainties, spatial heterogeneity and clear-sky bias](https://www.sciencedirect.com/science/article/pii/S1569843223001693)  

**Shuo Xu**, Dongdong Wang, Shunlin Liang, Yuling Liu, Aolin Jia.
<br><em>International Journal of Applied Earth Observation and Geoinformation, 2023, Impact Factor = 8.6</em>.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">IEEE GRSL 2023</div>
      <!-- <img src='images/trend.png' alt="sym" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Assessing the reliability of the MODIS LST product to detect temporal variability](https://ieeexplore.ieee.org/abstract/document/10242120)  

**Shuo Xu**, Dongdong Wang, Shunlin Liang, Yuling Liu, Aolin Jia.
<br><em>IEEE Geoscience and Remote Sensing Letters, 2023, Impact Factor = 4.4</em>.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">RS 2021</div>
      <!-- <img src='images/rf.png' alt="LST Review" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[A random forest-based data fusion method for obtaining all-weather land surface temperature with high spatial resolution](https://www.mdpi.com/2072-4292/13/11/2211)  

**Shuo Xu**, Jie Cheng, Qiang Zhang.
<br><em>Remote Sensing, 2021, Impact Factor = 4.1</em>.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">IEEE JSTARS 2019</div>
      <!-- <img src='images/bme.png' alt="LST Review" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Reconstructing all-weather land surface temperature using the Bayesian maximum entropy method over the Tibetan Plateau and Heihe River Basin](https://ieeexplore.ieee.org/document/8745679)  

**Shuo Xu**, Jie Cheng, Qiang Zhang.
<br><em>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2019, Impact Factor = 5.3</em>.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">IEEE GRSM 2024</div>
      <!-- <img src='images/review.png' alt="LST Review" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Advances in methodology and generation of all-weather land surface temperature products from polar-orbiting and geostationary satellites: A comprehensive review](https://ieeexplore.ieee.org/document/10679195)  

Aolin Jia, Shunlin Liang, Dongdong Wang, Kanishka Mallick, Shugui Zhou, Tian Hu, **Shuo Xu**.
<br><em>IEEE Geoscience and Remote Sensing Magazine, 2024, Impact Factor = 16.4</em>. 
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">ESSD 2023</div>
      <!-- <img src='images/essd.png' alt="LST Review" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[Global hourly, 5 km, all-sky land surface temperature data from 2011 to 2021 based on integrating geostationary and polar-orbiting satellite data](https://essd.copernicus.org/articles/15/869/2023/)  

Aolin Jia, Shunlin Liang, Dongdong Wang, Lei Ma, Zhihao Wang, **Shuo Xu**.
<br><em>Earth System Science Data, 2023, Impact Factor = 11.6</em>.
</div>
</div>

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge badge-journal">IEEE JSTARS 2020</div>
      <!-- <img src='images/downscaling.png' alt="LST Review" width="100%"> -->
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

[A stepwise downscaling method for generating high-resolution land surface temperature from AMSR-E data](https://ieeexplore.ieee.org/document/9190035)  

Qiang Zhang, Ning Wang, Jie Cheng, **Shuo Xu**.
<br><em>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2020, Impact Factor = 5.3</em>.
</div>
</div>


<div style="clear: both;"></div>


---

<span class='anchor' id='awards'></span>
# 🏅 Honors and Awards

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

---

<span class='anchor' id='educations'></span>
# 📖 Educations

- *2021.09 - Present*   Ph.D. candidate, Geographic Information Science and Cartography, **University of Maryland**, College Park, MD, USA
- *2018.09 - 2021.06*   M.S., Cartography and Geography Information System, **Beijing Normal University**, Beijing, China
- *2014.09 - 2018.06*   B.S., Remote Sensing Science and Technology, **Shandong University of Science and Technology**, Qingdao, China

---

<span class='anchor' id='work-experience'></span>
# 💼 Work Experience

### Research Assistant - University of Maryland  
*Sep 2021 - Present*  
**NSF-Funded Project: Improving the Ecosystem Demography (ED) Model with AI**  
- Developed transformer-based ML frameworks integrating satellite, model, and in-situ data.  
- Generated time series of carbon stocks, fluxes, and vegetation dynamics.  
- Applied spatial and temporal analyses.

**NOAA-Funded Project: Enhancing NOAA VIIRS Land Surface Temperature Product**  
- Designed multi-source fusion algorithms for all-weather VIIRS LST product.  
- Built data pipelines (Python/TensorFlow, MATLAB) to produce global LST time series and anomalies.  
- Presented findings at AGU and AMS conferences.


---

# 🎙️ Conference Presentations

- **Shuo Xu**, Yuling Liu. All-weather VIIRS LST: Machine Learning Based Methodology and Experiment. *105th American Meteorological Society (AMS) Annual Meeting, New Orleans, Jan 2025*.  
- **Shuo Xu**, Yuling Liu, Yunyue Yu, Peng Yu. All-weather LST: Methodology and Experiment on JPSS/VIIRS LST. *American Geophysical Union (AGU) Fall Meeting, Washington DC, Dec 2024*.  
- **Shuo Xu**, Yuling Liu, Yunyue Yu, Peng Yu. All-weather LST: Methodology and Experiment. *National Oceanic and Atmospheric Administration (NOAA) Cooperative Research Programs (CoRP) Science Symposium, Madison, WI, July 2023*.  
- **Shuo Xu**, Dongdong Wang. Validation of gridded datasets of near-surface temperature variables: uncertainties, spatial heterogeneity and clear-sky bias. *American Geophysical Union (AGU) Fall Meeting, Chicago, IL, Dec 2022*.  
- Yuling Liu, Yunyue Yu, Peng Yu, **Shuo Xu**, Heshun Wang. Validation and Performance Evaluation of NOAA-21 VIIRS LST Product. *American Geophysical Union (AGU) Fall Meeting, Washington DC, Dec 2024*.  

---

<span class='anchor' id='service'></span>
# 🤝 Peer Review & Scientific Committee Service

- **IGARSS 2025 Scientific Committee**
- **GeoIndustry Workshop at ACM SIGSPATIAL 2025 Program Reviewer**
- **Reviewer for 14 International Journals**, including:  
  - Remote Sensing of Environment  
  - Earth System Science Data  
  - IEEE Transactions on Geoscience and Remote Sensing  
  - Scientific Data  
  - IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing  
  - GPS Solutions  
  - Scientific Reports  
  - Journal of Geophysical Research: Atmospheres  
  - Environmental Monitoring and Assessment  
  - Earth Science Informatics  
  - Photogrammetric Engineering and Remote Sensing  
  - Discover Cities  
  - Environmental Earth Sciences  
  - Theoretical and Applied Climatology    

---







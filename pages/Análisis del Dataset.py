import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NutriFacts", page_icon=":pineapple:", layout="wide")

st.title ("Información adicional de los datos")
#st.header("You may also interact with your Tableau Public repos, just like this: ")
def main():
    html_temp='''<div class='tableauPlaceholder' id='viz1720259024416' style='position: relative'><noscript><a href='#'><img alt='Información Dataset ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Nu&#47;NutriFacts&#47;InformacinDataset&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NutriFacts&#47;InformacinDataset' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Nu&#47;NutriFacts&#47;InformacinDataset&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1720259024416');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='1527px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''    
    components.html(html_temp, width=1366, height=700)

if __name__ == '__main__':
    main()

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NutriFacts", page_icon=":pineapple:", layout="wide")

st.title ("Información adicional por país")
#st.header("You may also interact with your Tableau Public repos, just like this: ")
def main():
    html_temp='''<div class='tableauPlaceholder' id='viz1720438544140' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Paises_17204275320880&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Paises_17204275320880&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Paises_17204275320880&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1720438544140');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='827px';vizElement.style.height='2096px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='827px';vizElement.style.height='2096px';} else { vizElement.style.width='100%';vizElement.style.height='2127px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''    
    components.html(html_temp, width=827, height=2069)

if __name__ == '__main__':
    main()

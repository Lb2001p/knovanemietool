import streamlit as st
import pandas as pd
import numpy as np

def bepaal_beleid(is_hoog_risico, hb, mcv, ferritine):
    """Geeft exact beleid volgens KNOV-richtlijnen met vaste Hb-grens van 7.1"""
    # Classificaties
    hb_laag = hb < 7.1
    ferritine_laag = ferritine < 30

    # MCV classificatie
    if mcv < 70:
        mcv_status = "<70"
    elif 70 <= mcv <= 79:
        mcv_status = "70-79"
    elif 80 <= mcv <= 100:
        mcv_status = "80-100"
    else:
        mcv_status = ">100"
    
    # HOOG RISICO logica
    if is_hoog_risico:
        if hb_laag:
            if mcv_status == "<70":
                if ferritine_laag:
                    return "1. Screen op HbP\n2. Start ferrofumaraat."
                else:
                    return ("1. Screen op HbP.\n2. Onderzoek oorzaak anemie.\n"
                           "3. Behandel/verwijs.\n4. Overweeg ferrofumaraat.")
            
            elif mcv_status == "70-79":
                if ferritine_laag:
                    return "1. Overweeg HbP screening.\n2. Start ferrofumaraat."
                else:
                    return ("1. Onderzoek oorzaak anemie.\n2. Behandel/verwijs.\n"
                           "3. Overweeg HbP screening.\n4. Overweeg ferrofumaraat.")
            
            elif mcv_status == "80-100":
                if ferritine_laag:
                    return "Start ferrofumaraat."
                else:
                    return ("1. Onderzoek oorzaak anemie.\n2. Behandel/verwijs.\n"
                           "3. Overweeg ferrofumaraat.")
            
            else:  # >100
                if ferritine_laag:
                    return ("1. Start ferrofumaraat.\n"
                           "2. Bepaal vitamine B12 en foliumzuur.\n"
                           "3. Behandel/verwijs voor B12/foliumzuur.")
                else:
                    return ("1. Onderzoek oorzaak anemie (oa B11/B12).\n"
                           "2. Behandel/verwijs zo nodig.\n"
                           "3. Overweeg start ferrofumeraat.")
        
        else:  # Hb normaal (hoogrisico)
            if mcv_status == "<70":
                if ferritine_laag:
                    return "1. Screen op HbP.\n2. Overweeg ferrofumaraat."
                else:
                    return "1. Screen op HbP.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk."
            
            elif mcv_status == "70-79":
                if ferritine_laag:
                    return "1. Overweeg HbP screening.\n2. Overweeg ferrofumaraat."
                else:
                    return "1. Overweeg HbP screening.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk."
            
            elif mcv_status == "80-100":
                if ferritine_laag:
                    return "Overweeg ferrofumaraat."
                else:
                    return "Herhaal lab Hb+MCV+Ferritine 20-27 wk."
            
            else:  # >100
                if ferritine_laag:
                    return ("1. Overweeg start ferrofumaraat.\n"
                           "2. Bepaal vitamine B12 en foliumzuur.\n"
                           "3. Behandel/verwijs zo nodig.")
                else:
                    return ("1. Bepaal vitamine B12 en foliumzuur.\n"
                           "2. Behandel/verwijs zo nodig.\n"
                           "3. Herhaal lab Hb+MCV+Ferritine 20-27 wk.")
    
    # LAAG RISICO logica
    else:
        if hb_laag:
            if mcv_status == "<70":
                if ferritine_laag:
                    return "Start ferrofumaraat."
                else:
                    return ("1. Overweeg ferrofumaraat.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk.\n"
                           "3. Onderzoek oorzaak.\n4. Behandel/verwijs.")
            
            elif mcv_status == "70-79":
                if ferritine_laag:
                    return "Start ferrofumaraat."
                else:
                    return ("1. Overweeg ferrofumaraat.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk.\n"
                           "3. Onderzoek oorzaak.\n4. Behandel/verwijs.")
            
            elif mcv_status == "80-100":
                if ferritine_laag:
                    return "Start ferrofumaraat."
                else:
                    return ("1. Overweeg ferrofumaraat.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk.\n"
                           "3. Onderzoek oorzaak.\n4. Behandel/verwijs.")
            
            else:  # >100
                if ferritine_laag:
                    return ("1. Bepaal vitamine B12 en foliumzuur.\n"
                           "2. Start ferrofumaraat.\n"
                           "3. Behandel/verwijs voor B12/foliumzuur.")
                else:
                    return ("1. Bepaal vitamine B12 en foliumzuur.\n"
                           "2. Overweeg start ferrofumeraat.\n"
                           "3. Behandel/verwijs zo nodig.\n"
                           "4. Herhaal lab Hb+MCV+Ferritine 20-27 wk.")
        
        else:  # Hb normaal (laagrisico)
            if mcv_status == "<70":
                if ferritine_laag:
                    return "1. Overweeg ferrofumaraat.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk."
                else:
                    return "Herhaal lab Hb+MCV+Ferritine 20-27 wk."
            
            elif mcv_status == "70-79":
                if ferritine_laag:
                    return "1. Overweeg ferrofumaraat.\n2. Herhaal lab Hb+MCV+Ferritine 20-27 wk."
                else:
                    return "Herhaal lab Hb+MCV+Ferritine 20-27 wk."
            
            elif mcv_status == "80-100":
                return "Herhaal lab Hb+MCV+Ferritine 20-27 wk."
            
            else:  # >100
                return ("1. Bepaal B12/foliumzuur.\n"
                "2. Behandel of verwijs zo nodig.\n"
                "3. Herhaal lab Hb+MCV+Ferritine 20-27 wk.")

# UI Setup
st.set_page_config(page_title="KNOV Anemie Tool", layout="centered")
st.title("KNOV Anemie Beleidstool")

# Tabbladen aanmaken
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Intakelab", "Tweede en derde trimester", "Postpartum", "Hb afkapwaarden", "Ijzersuppletie", "Literatuur"])

with tab1:
    st.warning("Let op: deze pagina is alleen bedoeld voor beleidsbepaling n.a.v. het intakelab afgenomen VÓÓR 13 weken. Zie voor beleid in het tweede en derde trimester het tabblad 'Tweede en derde trimester'")
   
    # Risicofactoren
    with st.expander("📋 Risicofactoren voor anemie", expanded=False):
        st.markdown("""
        - Anemie/ijzergebrek in voorgeschiedenis
        - Niet-Noord-Europese afkomst
        - Multipara (≥3 bevallingen)
        - Meerlingzwangerschap
        - Leeftijd <25 jaar
        - Slechte en/of afwijkende voedingsgewoontes, inclusief recente bariatrische chirurgie en vegetarisch/veganistisch eetpatroon
        - Opnieuw zwanger binnen 1 jaar sinds bevalling
        - Recente geschiedenis van klinisch significante bloedingen (inclusief zware menstruaties)
        - Ziekte van Crohn/colitis ulcerosa (en andere darmaandoeningen)
        - Reumatoïde artritis
        - Een hoog risico op bloedingen tijdens zwangerschap (zoals placenta praevia of trombocytopenie) of geboorte (zoals HPP in anamnese, BMI>40, uterus myomatosus)
        - Weigering van bloedproducten
        - Wanneer verstrekken van compatibel bloed een uitdaging is (zoals vrouwen met irregulaire erytrocyten antistoffen)
        - Zwangeren die bekend zijn met hemoglobinopathie/ drager zijn van hemoglobinopathie óf vrouwen die gescreend worden op HbP-dragerschap
        """)

    heeft_risicofactoren = st.radio(
        "Heeft de patiënt één of meer van bovenstaande risicofactoren?",
        ["Nee", "Ja"],
        index=0,
        horizontal=True
    )

    # Labwaarden
    st.header("Laboratoriumwaarden")
    st.markdown("""
    *Let op:* een ferritinebepaling wordt **NIET** standaard geïndiceerd in de laagrisicogroep, 
    maar zal bij een afwijkende MCV (<80 fL of >100 fL) altijd de eerste stap zijn in beleidsbepaling. 
    De KNOV adviseert wel het bundelen van labbepalingen i.v.m. belasting van de client en kosten voor de bepaling, overweeg dit!
    
    Gebruik de tool wanneer alle drie de waardes bekend zijn. """)

    col1, col2, col3 = st.columns(3)
    with col1:
        hb = st.number_input("Hb (mmol/L)", min_value=4.0, max_value=20.0, value=7.1, step=0.1)
    with col2:
        mcv = st.number_input("MCV (fL)", min_value=30, max_value=150, value=85)
    with col3:
        ferritine = st.number_input("Ferritine (µg/L)", min_value=0, value=30)

    if st.button("Bereken beleid"):
        is_hoog_risico = heeft_risicofactoren == "Ja"
        beleid = bepaal_beleid(is_hoog_risico, hb, mcv, ferritine)

        # Labwaarden in compacte weergave
        st.markdown(f"""
        **Risicoprofiel:** {'Hoogrisico' if is_hoog_risico else 'Laagrisico'}  
        **Hb:** {hb:.1f} mmol/L {'(laag)' if hb < 7.1 else '(normaal)'}  
        **MCV:** {mcv} fL  
        **Ferritine:** {ferritine} µg/L {'(laag)' if ferritine < 30 else '(normaal)'}
        """)

        # Advies met compacte scheiding
        st.markdown("<hr style='margin-top:5px; margin-bottom:5px'>", unsafe_allow_html=True)
        st.markdown("### ADVIES")
        for line in beleid.split('\n'):
            st.markdown(f"- {line}")

        # Opmerking in kleiner lettertype
        st.markdown("""
        <div style='font-size:14px; margin-top:10px'>
        <b>Opmerking:</b><br>
        Indien er niet wordt gestart met Ferrofumeraat of een ander beleid wordt gevoerd, zal een herbepaling van Hb+MCV tussen 20-27 wk altijd geïndiceerd zijn.<br>
        Een ferritinebepaling wordt vrijwel altijd geïndiceerd, behalve bij:
        <ul style='margin-top:5px; margin-bottom:5px'>
        <li>Laagrisicogroep</li>
        <li>Goed Hb (≥7.1 mmol/L)</li>
        <li>MCV 70-100 fL</li>
        <li>Goed bekend ferritine (≥30 µg/L)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Voetnoot
    st.divider()
    st.markdown("""
    *Verduidelijkingen:*  
    *HbP: Hemoglobinopathie zoals sikkelcelanemie of thallasemie. HbP screening door verloskundige, gynaecoloog of huisarts, indien de HbP status nog onbekend is. Een HPLA test is voldoende. Let op: Indien er sprake is van een HbP dan is dragerschapsonderzoek van partner geïndiceerd.   
    *Ferrofumaraat suppletie conform protocol: 200mg ferrofumaraat 3-7 keer per week. 
    *Bij voorkeur ingenomen op een lege maag met water of een bron van vitamine c (200-500mg). Na start ferrofumaraat: herhaal Hb+MCV+ferritine na 4-6 weken. Zie tab 'ijzeruppletie' voor meer informatie en alternatieven.*
    """)

with tab2:
    st.header("Trimester-specifiek beleid")
    
    trimester_col1, trimester_col2 = st.columns(2)
    
    with trimester_col1:
        st.subheader("2e trimester (13-27 weken)")
        st.markdown("""
        **Belangrijkste aandachtspunten:**
        - Screenen op anemie tussen 20-27 weken
        - Bij Hb onder de grens: start behandeling (zie tabblad 'Hb-afkapwaarden')
        - Ferritine < 30 µg/L: overweeg ijzersuppletie
        - MCV < 70 fL: screen op hemoglobinopathie
        
        **Follow-up:**
        - Herhaal lab na 4-6 weken bij start behandeling
        - Bij hoogrisico: mogelijk eerder herhalen
        """)
    
    with trimester_col2:
        st.subheader("3e trimester (28+ weken)")
        st.markdown("""
        **Belangrijkste aandachtspunten:**
        - Hb < 6.3 mmol/L: altijd behandelen (overweeg Ferinject ivm termijn)
        - Ferritine < 30 µg/L: start ijzersuppletie
        - MCV afwijkingen: oorzaak onderzoeken
        
        **Follow-up:**
        - Bij behandeling: controleer Hb voor partus
        - Overweeg IV ijzer bij slechte opname
        - Plan partusbeleid bij persisterende anemie
        
        **Postpartum:**
        - Controleer Hb na 24-48 uur bij significant bloedverlies
        - Continueer ijzersuppletie zo nodig
        """)

with tab3:
    st.header("Postpartum beleid")
    
    postpartum_col1, postpartum_col2 = st.columns(2)
    
    with postpartum_col1:
        st.subheader("Direct postpartum")
        st.markdown("""
        **Beleid bij bloedverlies:**
        - Hb < 5.6 mmol/L: direct verwijzen
        - Hb 5.6-6.5 mmol/L: overweeg verwijzing
        - Symptomatische anemie: altijd behandelen
        
        **Ijzersuppletie:**
        - Start bij Hb < 6.5 mmol/L
        - Overweeg bij Hb 6.5-7.2 mmol/L + klachten
        - IV ijzer bij slechte tolerantie/opname
        """)
    
    with postpartum_col2:
        st.subheader("Late postpartum (6 weken)")
        st.markdown("""
        **Controle:**
        - Hb < 7.2 mmol/L: verder onderzoek
        - Ferritine < 30 µg/L: continueer ijzer
        - MCV afwijkingen: oorzaak onderzoeken
        
        **Follow-up:**
        - Bij aanhoudende anemie: verwijzen
        - Bij klachten: controle na 3 maanden
        - Advies over anticonceptie en interval
        """)

with tab4:
    st.header("Hb afkapwaarden rondom de zwangerschap")
    st.markdown("""  
    ### Richtlijnen voor Hb-afkapwaarden conform de richtlijn  

    **Absolute verwijsindicatie:**
    - Hb < 5.6 mmol/L tijdens gehele zwangerschap: direct verwijzen naar tweede lijn  
    """)  

    st.markdown("""
    #### Preconceptioneel:
    <table>
    <tr><th>Groep</th><th>Hb (mmol/L)</th></tr>
    <tr><td>Vrouwen</td><td>&lt;7,5</td></tr>
    </table>

    #### Tijdens zwangerschap:
    <table>
    <tr><th>Amenorroeduur</th><th>Hb (mmol/L)</th></tr>
    <tr><td>≤13 weken</td><td>7,1</td></tr>
    <tr><td>14-17 weken</td><td>6,8</td></tr>
    <tr><td>18-21 weken</td><td>6,5</td></tr>
    <tr><td>22-37 weken</td><td>6,3*</td></tr>
    <tr><td>≥38 weken</td><td>6,5</td></tr>
    </table>

    #### Post partum:
    <table>
    <tr><th>Aantal weken</th><th>Hb (mmol/L)</th></tr>
    <tr><td>1-5 weken</td><td>6,5</td></tr>
    <tr><td>6 weken</td><td>7,2</td></tr>
    </table>

    **Opmerkingen:**
    - *6,3 mmol/L als laagste waarde is conform de landelijke richtlijn. Het lokale VSV-protocol kan hiervan afwijken. VSV's regio Utrecht hanteren een afkapwaarde van 6,5 mmol/L in het 2e-3e trimester
    - Deze waarden gelden voor zowel hoog- als laagrisico patiënten
    - Bij hoogrisico patiënten wordt eerder ingegrepen bij lagere ferritine of MCV-afwijkingen
    - De preconceptionele waarde conform de NHG-standaard anemie
    """, unsafe_allow_html=True)

with tab5:
    st.header("Ijzersuppletie protocol")
    
    suppletie_col1, suppletie_col2 = st.columns(2)
    
    with suppletie_col1:
        st.subheader("Orale ijzersuppletie")
        st.markdown("""
        **Ferrofumaraat:**
        - Standaard eerste keus
        - Dosering: 200mg 3-7x per week
        - Bij voorkeur op lege maag met vitamine C
        
        **Alternatieven:**
        - IJzerbisglycinaat bij intolerantie
        - IJzerfumaraat bij maagklachten
        - Vloeibaar ijzer voor doseerflexibiliteit
        
        **Bijwerkingen:**
        - Obstipatie (gebruek laxantia)
        - Maagklachten (neem bij maaltijd)
        - Donkere ontlasting (normaal)
        """)
    
    with suppletie_col2:
        st.subheader("Intraveneus ijzer")
        st.markdown("""
        **Indicaties:**
        - Intolerantie voor oraal ijzer
        - Malabsorptie
        - Ernstige anemie (Hb < 6.0)
        - Laat in zwangerschap
        
        **Opties:**
        - Ferricarboxymaltose (Ferinject)
        - IJzer(III)-isomaltoside (Monofer)
        
        **Follow-up:**
        - Controle Hb na 2-4 weken
        - Herhaal ferritine na 3 maanden
        - Bijwerkingen: hoofdpijn, flush
        """)

with tab6:
    st.header("Literatuur")
    st.markdown("""
    **Bronnen:**  
    Alle informatie in deze tool is terug te vinden via de volgende bronnen.
    """)
    
    st.markdown("""
    - Abbas, A. M., Abdelbadee, S. A., Alanwar, A., & Mostafa, S. (2018). Efficacy of ferrous bis-glycinate versus ferrous glycine sulfate in the treatment of iron deficiency anemia with pregnancy: a randomized double-blind clinical trial. The Journal of Maternal-Fetal & Neonatal Medicine, 32(24), 4139–4145. https://doi.org/10.1080/14767058.2018.1482871
    - Achebe, M. M., & Gafter-Gvili, A. (2016). How I treat anemia in pregnancy: iron, cobalamin, and folate. Blood, 129(8), 940–949. https://doi.org/10.1182/blood-2016-08-672246
    - Jung, J., Rahman, M. M., Rahman, M. S., Swe, K. T., Islam, M. R., Rahman, M. O., & Akter, S. (2019). Effects of hemoglobin levels during pregnancy on adverse maternal and infant outcomes: a systematic review and meta‐analysis. Annals of the New York Academy of Sciences, 1450(1), 69–82. https://doi.org/10.1111/nyas.14112
    - Karakoc, G., Orgul, G., Sahin, D., & Yucel, A. (2021). Is every other day iron supplementation effective for the treatment of the iron deficiency anemia in pregnancy? The Journal of Maternal-Fetal & Neonatal Medicine, 35(5), 832–836. https://doi.org/10.1080/14767058.2021.1910666
    - KNOV. (2025a, August 5). *Flowchart Anemie – Eerste trimester – 'Hoog risico'*  
      https://assets.knov.nl/p/557056/none/KNOV%20Flowchart%20Anemie%20-%20Hoog%20risico%20-%20juli%202025.pdf
    - KNOV. (2025b, August 5). *Flowchart Anemie – Eerste trimester – 'Laag risico'*  
      https://assets.knov.nl/p/557056/none/KNOV%20Flowchart%20Anemie%20-%20Laag%20risico%20-%20juli%202025.pdf
    - KNOV. (2025c). *MDR Anemie*  
      https://assets.knov.nl/p/557056/none/Richtlijn%20Anemie%20juni%202025.pdf
    - Koninklijke Nederlandse Organisatie van Verloskundigen. (n.d.). *Anemie*  
      https://www.knov.nl/kennis-en-scholing/vakkennis-en-wetenschap/vakkennis/anemie-knov-standaard
    - Naveed, K., Goldberg, N., Shore, E., Dhoot, A., Gabrielson, D., Goodarzi, Z., Lin, Y., Pai, M., Pardy, N. A., Robinson, S., Andreou, R., Sood, M., Price, V., Storm, S., Verduyn, A., Parker, M. L., Fralick, M., Beriault, D., & Sholzberg, M. (2023). Defining ferritin clinical decision limits to improve diagnosis and treatment of iron deficiency: A modified Delphi study. International Journal of Laboratory Hematology, 45(3), 377–386. https://doi.org/10.1111/ijlh.14016
    - NHG. (2024, September). *Anemie. NHG-Richtlijnen*  
      https://richtlijnen.nhg.org/standaarden/anemie
    - VSV Uniek, VSV Eendracht, & VSV Alliant. (2023). *Regioprotocol Anemie*
    - Young, M. F., Oaks, B. M., Rogers, H. P., Tandon, S., Martorell, R., Dewey, K. G., & Wendt, A. S. (2023). Maternal low and high hemoglobin concentrations and associations with adverse maternal and infant health outcomes: an updated global systematic review and meta-analysis. BMC Pregnancy and Childbirth, 23(1). https://doi.org/10.1186/s12884-023-05489-6
    """)
    
# Alternatieve footer
st.divider()  # Alternatief voor de horizontale lijn (Streamlit v1.23+)
st.caption("Augustus 2025 | Lotte Brink | Utrecht")

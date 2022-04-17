import streamlit as st
import json


def main():

    st.write(
        """
        ## Generate infrastructure
        """
    )
    CONTENT = {}
    st.text_input("Project name", key = "project_name")
    param1, Param2 = st.columns(2)
    with param1:
        add_storage = st.checkbox("add _storage")
    with Param2:
        add_compute = st.checkbox("add_compute")

    if add_storage:
        with st.container():

            col1, col2, col3 = st.columns(3)
            with col1:
                name = st.text_input("Choose a name (⬇💬👇ℹ️ ...)", value="⬇")
            with col2:
                type = st.selectbox("storage", ["S3", "sql-db"])
            with col3:
                st.write("")
                st.write("")
                st.write("")
                advanced = st.checkbox("advanced", key="storage")
                if advanced:
                    with st.container():
                        advanced = st.multiselect('storage advenced setting', ["vpn", "securite_group", "access_policy"])
        CONTENT["Storage"] = {"name":     name,
                              "type":     type,
                              "advanced": advanced,
                              }
    if add_compute:
        with st.container():

            comp1, comp2, comp3 = st.columns(3)
            with comp1:
                name = st.text_input("compute name (⬇💬👇ℹ️ ...)", value="⬇")
            with comp2:
                type = st.selectbox("compute type", ["ec2", "lambda"])
            with comp3:
                st.write("")
                st.write("")
                st.write("")
                advanced = st.checkbox("advanced", key="compute")
                if advanced:
                    with st.container():
                        advanced = st.multiselect('compute advenced setting', ["vpn", "securite_group", "access_policy"])


        CONTENT["Compute"] = {"name":     name,
                              "type":     type,
                              "advanced": advanced,
                              }

    CONTENT["metadata"] = {"Project_name": st.session_state.project_name,
                            }

        # if len(ll) > 1:
        #     for i in ll:
        #         x = [{
        #         "name" : st.text_input(f"add {i} name"),
        #         "type" : i}]
        #         CONTENT["Storage"] = x





    st.write("Press button to generate templates files")
    # st.button("Generate File")
    if CONTENT not in st.session_state:
        st.session_state.CONTENT = CONTENT
    if st.button("Generate File"):
        st.write(st.session_state.CONTENT)
        with open('person.json', 'w') as json_file:
            json.dump(st.session_state.CONTENT, json_file)


if __name__ == "__main__":
    main()

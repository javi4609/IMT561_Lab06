import pandas as pd
import streamlit as st

from src.charts import plot_response_hist, plot_borough_bar, plot_borough_count_bar


def header_metrics(df: pd.DataFrame) -> None:
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    # TODO (IN-CLASS): Replace these placeholders with real metrics from df
    # Suggestions:
    # - Total complaints (len(df))
    # - Median response time
    # - % from Web vs Phone vs App (pick one)

    total_complaints = len(df)
    median_response = round(df['response_time_days'].median(), 2)
    most_common = df['complaint_type'].value_counts().index.tolist()[0]

    with c1:
        st.metric("Total complaints", f"{total_complaints}")
    with c2:
        st.metric("Median response (days)", f"{median_response}")
    with c3:
        st.metric("Most common complaint", f"{most_common}")


def body_layout_tabs(df: pd.DataFrame) -> None:
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Distribution", "By Borough", "Table"])

    with t1:
        st.subheader("Response Time Distribution")
        plot_response_hist(df)

        # TODO (IN-CLASS): Add a short interpretation sentence under the chart
        st.text('This graph shows the count distribution of response times (measured in days). It can be filtered by borough, channel and complaint type')



    with t2:
        st.subheader("Median Response Time by Borough")
        plot_borough_bar(df)

        # TODO (IN-CLASS): Add a second view here (e.g., count by borough)
        st.subheader("Count by Borough")
        plot_borough_count_bar(df)


    with t3:
        st.subheader("Filtered Rows")
        st.dataframe(df, width='stretch', height=480)

        # TODO (OPTIONAL): Add st.download_button to export filtered rows

        st.download_button(
            label="Download CSV",
            data=df.to_csv().encode("utf-8"),
            file_name="data.csv",
            mime="text/csv",
            icon=":material/download:",
        )
import Layout from "../components/layout/Layout";
import StatCards from "../components/dashboard/StatCards";
import UploadPanel from "../components/dashboard/UploadPanel";

function Dashboard(){
    return (
        <Layout>
            <h1> Dashboard </h1>
            < StatCards />
            <UploadPanel />
        </Layout>
    );
}

export default Dashboard;
import Layout from '@layouts/MainLayout/index.jsx';
import MoviesList from "@widgets/MoviesList/MoviesList.jsx";

export default function MoviesPage() {
    return (
        <Layout>
            <MoviesList/>
        </Layout>
    );
}
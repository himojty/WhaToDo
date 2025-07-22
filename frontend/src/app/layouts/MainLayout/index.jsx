import Header from "@shared/ui/Header/Header.jsx";
import Footer from "@shared/ui/Footer/Footer.jsx";
import '../../styles/globals.css'


export default function Layout({children}) {
    return (
        <>
            <Header/>
            <main>
                {children}
            </main>
            <Footer/>
        </>
    )
};
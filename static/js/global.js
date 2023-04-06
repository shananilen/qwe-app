$(document).ready(function () {
    var currURL = window.location.href;
    if (currURL.includes("connection/sources")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('conn_source').classList.add('active_nav_link');
        document.getElementById('collapseExampleConnection').classList.add('show');
    }
    else if (currURL.includes("connection/destinations")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('conn_destination').classList.add('active_nav_link');
        document.getElementById('collapseExampleConnection').classList.add('show');
    }

    else if (currURL.includes("connection/channels")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('conn_channel').classList.add('active_nav_link');
        document.getElementById('collapseExampleConnection').classList.add('show');
    }

    else if (currURL.includes("connection/catalog")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('conn_catalog').classList.add('active_nav_link');
        document.getElementById('collapseExampleConnection').classList.add('show');
    }

    else if (currURL.includes("connection")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('data_pipelines').classList.add('active_nav_link');
        document.getElementById('collapseExampleConnection').classList.add('show');
    }



    else if (currURL.includes("segmentation")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('nav_bar_segments').classList.add('active_nav_link');
    }
    else if (currURL.includes("user")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('nav_bar_user').classList.add('active_nav_link');
    }
    else if (currURL.includes("audiences")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('nav_bar_audience').classList.add('active_nav_link');
    }
    else if (currURL.includes("campaign")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('nav_bar_campaign').classList.add('active_nav_link');
    }
    else if (currURL.includes("analytics")){
        document.getElementById('nav_bar_home').classList.remove('active_nav_link');
        document.getElementById('nav_bar_analytics').classList.add('active_nav_link');
    }




//     $('#myDIV > a')
//         .click(function (e) {
//             $('#myDIV > a')
//                 .removeClass('active_nav_link');
//             $(this).addClass('active_nav_link');
//         });
// });

});
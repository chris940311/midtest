document.querySelectorAll('.menu a').forEach(item => {
    item.addEventListener('click', event => {
        event.preventDefault(); // 阻止默認操作，以防頁面跳轉
        const sectionId = event.target.getAttribute('href').substr(1); // 從 href 中獲取區域 ID
        const section = document.getElementById(sectionId); // 根據區域 ID 獲取對應的元素
        if (section) {
            window.scrollTo({ top: section.offsetTop, behavior: 'smooth' }); // 平滑滾動到區域元素的頂部
        }
    });
});
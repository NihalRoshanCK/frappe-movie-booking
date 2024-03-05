<template>
    <div class="banner-container">
        <div class="banner-content banner-content-scroll">
          <img style="height:30vh;" class="w-full rounded-md" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP._WzwKDmmM7TG2t0Hnvln0AHaB3%26pid%3DApi&f=1&ipt=efca18bd27849a0da4ae67f3688965d24001974d9fa50f5e51f4a1380a45cb53&ipo=images" alt="">
        </div>
        <div class="banner-content banner-content-scroll">
            <img style="height:30vh;" class="w-full rounded-md" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP._WzwKDmmM7TG2t0Hnvln0AHaB3%26pid%3DApi&f=1&ipt=efca18bd27849a0da4ae67f3688965d24001974d9fa50f5e51f4a1380a45cb53&ipo=images" alt="">
        </div>
        <div class="banner-content banner-content-scroll">
            <img style=" height:30vh;" class="w-full rounded-md" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP._WzwKDmmM7TG2t0Hnvln0AHaB3%26pid%3DApi&f=1&ipt=efca18bd27849a0da4ae67f3688965d24001974d9fa50f5e51f4a1380a45cb53&ipo=images" alt="">
        </div>
        <div class="banner-content banner-content-scroll">
            <img style="height:30vh;" class="w-full rounded-md" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP._WzwKDmmM7TG2t0Hnvln0AHaB3%26pid%3DApi&f=1&ipt=efca18bd27849a0da4ae67f3688965d24001974d9fa50f5e51f4a1380a45cb53&ipo=images" alt="">
        </div>
        <div class="banner-content banner-content-scroll">
            <img style=" height:30vh;" class="w-full rounded-md" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP._WzwKDmmM7TG2t0Hnvln0AHaB3%26pid%3DApi&f=1&ipt=efca18bd27849a0da4ae67f3688965d24001974d9fa50f5e51f4a1380a45cb53&ipo=images" alt="">
        </div>
    </div>
</template>

<script>
export default {

}
</script>



<style>
    .banner-container {
        width: 100%;
        margin-top:2px ;
        overflow: hidden;
        white-space: nowrap;
        background-color: #f2f2f2;
    }
    
    .banner-content {
        display: inline-block;
        padding: 2px;
        font-size: 24px;
    }
    
    /* Animation */
    @keyframes scroll {
        0% { transform: translateX(0%); }
        100% { transform: translateX(-100%); }
    }
    
    .banner-content-scroll {
        animation: scroll 10s linear infinite;
    }
</style>
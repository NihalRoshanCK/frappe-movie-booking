<template lang="">
    <div style="padding:0 15%; margin-top:1%;" className=" flex flex-row w-full h-96 bg-lime-600 justify-between">
        <div style="width:50%;gap:20px;" className='flex flex-row w-2/5 gap-12 justify-center items-center'>
            <img  style="width:10%" src="https://www.anther.tech/files/anther-logo-lh.png" alt="Logo"/>
            <div style="width:90%">
                <input   style="width:100%;" type="text" className="rounded"/>
            </div>
        </div>
        <div style='display:flex; gap:20px; ' className='flex flex-row justify-center items-center'>
            <p>Kerala</p>
            <Button  style='background-color:red; color:white;' className='bg-red-600'>Sign in</Button>
            <p>Handburger</p>
        </div>
    </div>  
    <div style="padding:0 15%; margin-top:1%;" class="bg-gray-200">
    <Listbar/>
</div>
</template>
<script>
import Listbar from './listbar.vue'

export default {
  components: { Listbar },
}
// <div style="padding:0 15%; margin-top:1%;" class="bg-gray-200"> 
//     <listbar/>
//   </div>
</script>

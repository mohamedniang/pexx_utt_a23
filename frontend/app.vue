<template>
  <div class="flex flex-col items-center justify-center h-screen bg-blue-300">
    <h1 class="text-3xl font-black text-gray-100">App de visualisation des données environnementales</h1>
    <small class="text-gray-200">En construction</small>
    <div class="flex flex-row gap-2">
      <button @click="test_backend('/')" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
      Test route 1
    </button>
      <button @click="test_backend('/abt')" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
      Test route 2
    </button>
    </div>
    <div class="bg-gray-50 m-2 p-2 hover:bg-gray-200 rounded">
      <small>{{ result }}</small>
    </div>
  </div>
</template>

<script lang="ts" setup>
var result = ref("result will go here ...")
async function test_backend(route: string) {
  result.value = await $fetch(`http://127.0.0.1:5000${route}`)
}
</script>

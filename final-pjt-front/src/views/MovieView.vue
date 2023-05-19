<template>
  <div>
    <h1>MovieView</h1>
    <div class="input-group search">
      <div>
        <input type="text" class="form-control" placeholder="영화 제목을 입력하세요."/>
      </div>
      <div>
        <i class="btn btn-light bi bi-search ms-2"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieView'
}
</script>

<style>
.search {
  display:flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}

.input-group {
  width: 100%;
}

.form-control {
  width: 100%;
}

</style>
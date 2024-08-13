<template>
  <div>
    <div class="FormContainer">
      <form @submit="(e) => handleSubmit(e)">
        <div class="brand">
          <h1>事件采集系统</h1>
        </div>
        <input type="text" placeholder="请输入事件标题" name="title" v-model="userForm.title"/>
        <input type="text" placeholder="请输入事件描述" name="description" v-model="userForm.description" />
        <span class="button">
          <button type="submit">上报事件</button>
          <button type="reset" @click="(e) => handleReset(e)">重置</button>
        </span>
      </form>
    </div>
  </div>
</template>

<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

import { ref } from 'vue'
import { notification } from 'ant-design-vue'

// 登录信息表单
const userForm = ref({
  title: '',
  description: ''
})

/**
 * @description:处理点击注册事件
 * @param {*} e 事件对象
 */
const handleSubmit = async (e) => {
  e.preventDefault()
  if (handleValidation(userForm)) {
   openNotificationWithIcon('success', '事件上报成功！')
  }
}
/**
 * @description: 校验登录信息表单
 * @param {Object} form 登录信息表单
 */
const handleValidation = (form) => {
  const { title, description } = form.value
  if (title === '' || description === '') {
    openNotificationWithIcon('error', '事件标题和描述不能为空')
    return false
  }
  return true
}
/**
 * @description: AntDesign的api，显示弹窗信息
 * @param {string} type 图标，可选值有success、info、warning、error
 * @param {string | VNode | () => VNode} message 通知提醒标题，必选
 */
const openNotificationWithIcon = (type, message) => {
  notification[type]({
    message,
    description: ''
  })
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
  .logo {
    margin: 0 2rem 0 0;
  }
  header .wrapper {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    background-color: white;
    border-radius: 2rem;
    width: 40vw;
    padding: 3rem 5rem;
    input {
      background-color: transparent;
      padding: 1rem;
      border: 0.1rem solid rgb(56, 72, 93);
      color: black;
      width: 100%;
      font-size: 1rem;
      &:focus {
        border: 0.1rem solid rgb(100, 182, 135);
        outline: none;
      }
    }
    .button {
      display: grid;
      grid-template-columns: 50% 50%;
    }
    button {
      background-color: rgb(56, 72, 93);
      color: white;
      margin: 0 2rem;
      padding: 1rem 2rem;
      border: none;
      font-weight: bold;
      cursor: pointer;
      border-radius: 0.4rem;
      font-size: 1rem;
      transition: 0.5s ease-in-out;
      &:hover {
        background-color: rgb(100, 182, 135);
      }
    }
    span {
      color: white;
      text-transform: uppercase;
      text-align: center;
      a {
        color: rgb(100, 182, 135);
        text-decoration: none;
        font-weight: bold;
      }
    }
  }
}
</style>

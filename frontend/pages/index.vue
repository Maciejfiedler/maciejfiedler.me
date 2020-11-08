<template>
  <c-dark-mode>
    <c-box
      p="20px"
      w="100vw"
      h="100vh"
      bgImage="url('https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&dl=jeremy-perkins-uhjiu8FjnsQ-unsplash.jpg')"
    >
      <c-box p="20px" bg="black" color="white" borderRadius="15px">
        <c-stack spacing="2">
          <c-heading as="h1" textAlign="center">Status:</c-heading>
          <c-code fontSize="48px" textAlign="center">Good </c-code>
        </c-stack>
      </c-box>
      <c-box p="20px">
        <c-image
          w="500px"
          mr="auto"
          ml="auto"
          src="https://raw.githubusercontent.com/Maciejfiedler/maciejfiedler.me/main/Assets/Logo%20(high%20resolution).png"
          alt="Logo"
      /></c-box> </c-box
  ></c-dark-mode>
</template>

<script lang="ts">
/* eslint-disable vue/no-unused-components */

import Chakra from '@chakra-ui/vue'

export default {
  name: 'App',
  components: {
    Chakra,
  },
  inject: ['$chakraColorMode', '$toggleColorMode'],
}
</script>

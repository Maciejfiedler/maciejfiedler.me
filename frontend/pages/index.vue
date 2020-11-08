<template>
  <c-dark-mode>
    <c-box p="20px" w="100vw" h="100vh" bg="blue.800" color="white">
      <c-box p="20px" bg="blue.900" borderRadius="15px">
        <c-stack spacing="2">
          <c-heading as="h1" textAlign="center">Status:</c-heading>
          <c-code fontSize="48px" textAlign="center">Good Good </c-code>
        </c-stack>
      </c-box>
    </c-box></c-dark-mode
  >
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

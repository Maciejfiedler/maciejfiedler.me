<template>
  <c-light-mode>
    <c-box p="20px" height="100vh" bg="green.50">
      <c-flex align="center" justify="center">
        <c-box p="20px" maxW="1000px">
          <c-stack spacing="2" pr="20px" pl="20px" textAlign="center">
            <c-heading as="h1" size="2xl">Not found</c-heading>
            <c-text fontSize="2xl"
              >The page you were looking for was not found. I'm sorry
              😔️</c-text
            >
            <c-code variant-color="green" fontSize="2xl">Error 404</c-code>
          </c-stack>
        </c-box></c-flex
      >
    </c-box></c-light-mode
  >
</template>

<script lang="ts">
/* eslint-disable vue/no-unused-components */
import Chakra from '@chakra-ui/vue'

export default {
  name: '404',
  head() {
    return {
      title: 'Not Found - Error 404',
    }
  },
  components: {
    Chakra,
  },
}
</script>
<style>
body {
  background: #e2fbed;
}
</style>
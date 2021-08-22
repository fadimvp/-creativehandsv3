// Cart shpping calculate
const shippingBtn = document.querySelector('.shipping-btn');
const openShipping = document.querySelector('.shpping-method');

shippingBtn.addEventListener("click", () => {
  openShipping.classList.toggle("active");
});


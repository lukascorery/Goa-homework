// 2) შექმენით getProducts ფუნქცია, რომელიც წამოათრევს ინფორმაციას მოცემული api-იდან, თქვენ მოგეცემათ სია 20 პროდუქტის ობიექტით, თქვენი დავალებაა თითოეული პროდუქტის სათაური, კატეგორია და სურათი დაარენდეროთ ცალ-ცალკე დივებად products container-ში (div), თქვენი სიტყვებით დაწერეთ async & await-ზე

// https://fakestoreapi.com/products
// დრო 10:55-მდე

function getProducts() {
    const productsContainer = document.getElementById('productsContainer');

    async function fetchProducts() {
        try {
            const response = await fetch('https://fakestoreapi.com/products');
            const products = await response.json();
            products.forEach(product => {
                const productDiv = document.createElement('div');
            }
            );
        } catch (error) {
            console.error('Error fetching products:', error);
        }
    }

    fetchProducts();
}
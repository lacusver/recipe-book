$(document).ready(function() {
    $('.js-basic-multiple').select2();

    const test = document.getElementsByClassName('formset-recipe-list');
    const testleng = test.length-1;
    console.log(testleng)
    const addMoreBtn = document.getElementById('add-more');
    const totalNewForms = document.getElementById('id_recipelist_set-TOTAL_FORMS');

    addMoreBtn.addEventListener('click', add_new_form);

    function add_new_form(event) {
        if(event){
            event.preventDefault();
        }
        const currentRecipeListForms = document.getElementsByClassName('formset-recipe-list');
        const countRecipeListForms = currentRecipeListForms.length;
        
        const formCopyTarget = document.getElementById('recipe-list-form');
        const copyRecipeListForm = document.getElementById(`form-${testleng}`).cloneNode(true);
        copyRecipeListForm.setAttribute('id', `form-${countRecipeListForms}`);
        const regex = new RegExp(`recipelist_set-${testleng}`, 'g');
        copyRecipeListForm.innerHTML = copyRecipeListForm.innerHTML.replace(regex, 'recipelist_set-'+countRecipeListForms);
        totalNewForms.setAttribute('value', countRecipeListForms+1);
        formCopyTarget.append(copyRecipeListForm);
    }

});
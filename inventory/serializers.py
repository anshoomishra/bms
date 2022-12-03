from rest_framework import serializers
from inventory.models import Ingredients, BakeryItem


class IngredientSerializers(serializers.ModelSerializer):
    """
    To Add Only Ingredient
    """
    class Meta:
        model = Ingredients
        fields = '__all__'


class BakeryItemsSerializers(serializers.ModelSerializer):
    """
    To Add bakery Items along with existing Ingredients
    """
    ingredients = IngredientSerializers(many=True)
    
    class Meta:
        model = BakeryItem
        fields = "__all__"
    
    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        print(ingredients)
        bakery_item = BakeryItem.objects.create(**validated_data)
        total_cost_price_of_ingredient = 0
        ingre_list = []
        for ingredient in ingredients:
            total_cost_price_of_ingredient += ingredient["quantity"]*ingredient["cost_price"]
            instance = Ingredients.objects.create(**ingredient)
            ingre_list.append(instance)
        
        bakery_item.ingredients.set(ingre_list)
        bakery_item.cost_price = total_cost_price_of_ingredient
        bakery_item.selling_price = total_cost_price_of_ingredient+(total_cost_price_of_ingredient*bakery_item.profit/100)
        bakery_item.save()
        return bakery_item
    
